import numpy as np
import matplotlib.pyplot as plt
class CLASS_FILTER:                                                             #滤波器类
    N = 0                                                                       #滤波器系数个数
    filterCoeff = 0                                                             #滤波器系数序列
    length = 0                                                                  #滤波器输入的数据缓冲区中有效输入数据的个数
    buff =np.zeros(20000)                                                       #滤波器输入的数据缓冲区
    def init(self, filterCoeff, N):
        self.N = N
        self.filterCoeff = filterCoeff
        
    def calc(self, u):
        self.length += 1
        self.buff[self.length - 1] = u
        sum = 0
        if(self.length < self.N):
            for i in range(self.length):
                sum += self.buff[i] * self.filterCoeff[self.length - 1 - i]
            for i in range(self.N - self.length):
                sum += self.buff[0] * self.filterCoeff[self.N - 1 - i]
        else:
            for i in range(self.length - self.N, self.length):
                sum += self.buff[i] * self.filterCoeff[self.length - 1 - i]
        return sum

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

def main():
    myFilter = CLASS_FILTER()
    Ts = 1 / 1000                                                               #采样频率为1kHz
    t = np.arange(0, 10, Ts)
    x = t
    yIn = np.sin(30 * 2 * np.pi * t)                                            #输入信号为30Hz的正弦信号
    filterCoeff = [0.2, 0.2, 0.2, 0.2, 0.2]
    filterN = len(filterCoeff)
    length = len(yIn)
    yOut = np.zeros(length)
    myFilter.init(filterCoeff, filterN)
    for i in range(length):
        yOut[i] = myFilter.calc(yIn[i])
    myPlot(x, yIn, xName='时间(s)', yName='输入信号', label='输入信号', figureNum=1, figurePosition=1)
    myPlot(x, yOut, xName='时间(s)', yName='输出信号', label='输出信号', figureNum=1, figurePosition=2)

main()
