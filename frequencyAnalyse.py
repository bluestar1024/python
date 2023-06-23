# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 00:23:11 2023

@author: YXD
"""

import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

def myPlot(x, y, xName=None, yName=None, label=None, figureNum=None, figurePosition=1):
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    fig = plt.figure() if figureNum == None else plt.figure(int(figureNum))
    if(1 == figurePosition):
        fig.clf()
    subFig = fig.add_subplot(2, 1, figurePosition)
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
    Ts = 1 / 1000                                                                                           #采样频率为1kHz
    t = np.arange(0, 1, Ts)
    u = 0.3 * np.sin(50 * 2 * np.pi * t) + 0.5 * np.sin(30 * 2 * np.pi * t)                                 #输入信号为50Hz和30Hz的正弦信号的叠加
    myPlot(t, u, xName='时间(s)', yName='输入信号', label='时域', figureNum=1, figurePosition=1)

    freq, amplitude = myFreqAnalysize(u, Ts)
    myPlot(freq, amplitude, xName='频率(Hz)', yName='幅值', label='频域', figureNum=1, figurePosition=2)

main()
