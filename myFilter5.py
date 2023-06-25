# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:00:33 2023

@author: YXD
"""

import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

class CLASS_FILTER:
    def init(self, Ts, Fc, N=0):
        self.Ts = Ts                                                                            #采样周期
        self.Fc = Fc                                                                            #截止频率
        self.HalfN = int(10 / (2 * self.Fc * self.Ts)) if N == 0 else int(np.ceil(N / 2))       #np.ceil为向上取整
        self.N = 2 * self.HalfN                                                                 #滤波器阶数
        self.M = self.N + 1                                                                     #滤波器系数个数
        self.BuffIndex = 0                                                                      #缓冲区索引
        self.Buff = np.zeros(self.M)                                                            #滤波器输入的数据闭环缓冲区，即该缓冲区索引达到最后时，下一次索引移动操作(索引每次加一)会将索引置0
        self.FilterCoeff = self.GetFilterCoeff()                                                #滤波器系数序列                                      
        self.FirstFlag = True                                                                   #处理第一个输入数据的标志
        self.Bais = 0                                                                           #存储偏置，即存储第一个输入数据
    
    def GetFilterCoeff(self):
        coeff = np.zeros(self.M)
        for i in range(1, self.HalfN + 1):
            coeff[self.HalfN + i] = (1 + np.cos(i * np.pi / self.HalfN)) / (i * 2 * np.pi) * np.sin(i * 2 * np.pi * self.Fc * self.Ts)
            coeff[self.HalfN - i] = coeff[self.HalfN + i]
        coeff[self.HalfN] = 2 * self.Fc * self.Ts
        coeff /= np.sum(coeff)                                                                  #使滤波器系数和为1
        return coeff
        
    def calc(self, u):
        if(self.FirstFlag):
            self.Bais = u
            self.FirstFlag = False
        def index(i):
            return (self.BuffIndex + i + self.M) % self.M
        self.Buff[self.BuffIndex] = u - self.Bais
        sum = 0
        
        for i in range(self.M):
            sum += self.Buff[index(-i)] * self.FilterCoeff[i]
                
        self.BuffIndex = (self.BuffIndex + 1) % self.M
        return sum + self.Bais

def myPlot(x, y, xName=None, yName=None, label=None, figureNum=None, figurePosition=1):
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    fig = plt.figure() if figureNum == None else plt.figure(int(figureNum))
    if(1 == figurePosition):
        fig.clf()
    subFig = fig.add_subplot(4, 1, figurePosition)
    subFig.plot(np.array(x), np.array(y), label=label)
    subFig.legend(loc="upper right")
    subFig.set_xlabel(xName)
    subFig.set_ylabel(yName)
    subFig.grid('on')
    plt.show()

def myFreqAnalysize(u, Ts):
    Fs = 1 / Ts
    N = len(u)
    amplitude = abs(fft.fft(u)) / N
    freq = np.arange(0, (int(N / 2) + 1) * Fs / N, Fs / N)
    amplitude = np.append(amplitude[0], amplitude[1 : int(N / 2) + 1] * 2)
    return freq, amplitude

def main():
    Ts = 1 / 1000                                                                               #采样频率为1kHz
    t = np.arange(0, 1, Ts)
    x = t                                          
    yIn = 0.3 * np.sin(50 * 2 * np.pi * t) + 0.5 * np.sin(30 * 2 * np.pi * t)                   #输入信号为50Hz和30Hz的正弦信号的叠加
    length = len(yIn)
    yOut = np.zeros(length)
    myFilter = CLASS_FILTER()
    myFilter.init(Ts, 40, N=0)
    for i in range(length):
        yOut[i] = myFilter.calc(yIn[i])
    
#################################################画图#######################################################
    myPlot(x, yIn, xName='时间(s)', yName='信号', label='输入时域', figureNum=1, figurePosition=1)
    myPlot(x, yOut, xName='时间(s)', yName='信号', label='输出时域', figureNum=1, figurePosition=2)
    freq, amplitude = myFreqAnalysize(yIn, Ts)
    myPlot(freq, amplitude, xName='频率(Hz)', yName='幅值', label='输入频域', figureNum=1, figurePosition=3)
    freq, amplitude = myFreqAnalysize(yOut, Ts)
    myPlot(freq, amplitude, xName='频率(Hz)', yName='幅值', label='输出频域', figureNum=1, figurePosition=4)

main()
