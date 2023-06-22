import numpy as np
class CLASS_FILTER:
    N = 0
    FC = 0
    length = 0
    buff =np.zeros(20000)
    def init(self, FC, N):
        self.N = N
        self.FC = FC
        
    def calc(self, u):
        self.length += 1
        self.buff[self.length - 1] = u
        sum = 0
        if(self.length < self.N):
            for i in range(self.length):
                sum += self.buff[i] * self.FC[self.length - 1 - i]
            for i in range(self.N - self.length):
                sum += self.buff[0] * self.FC[self.N - 1 - i]
        else:
            for i in range(self.length - self.N, self.length):
                sum += self.buff[i] * self.FC[self.length - 1 - i]
        return sum

def myPlot(x, y, xName=None, yName=None, label=None, figureNum=None, k=1):
    import matplotlib.pyplot as plt
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    fig = plt.figure() if figureNum == None else plt.figure(int(figureNum))
    if(1 == k):
        fig.clf()
    a = fig.add_subplot(2, 1, k)
    a.plot(np.array(x), np.array(y), label=label)
    a.legend(loc="upper right")
    a.set_xlabel(xName)
    a.set_ylabel(yName)
    a.grid('on')
    plt.show()

def main():
    myFilter = CLASS_FILTER()
    Ts = 1 / 1000
    t = np.arange(0, 10, Ts)
    x = t
    y = np.sin(t)
    filterCoeff = [0.2, 0.2, 0.2, 0.2, 0.2]
    filterN = len(filterCoeff)
    length = len(y)
    out = np.zeros(length)
    myFilter.init(filterCoeff, filterN)
    for i in range(length):
        out[i] = myFilter.calc(y[i])
    myPlot(x, y, xName='时间(s)', yName='输入信号输出', label='输入信号', figureNum=1, k=1)
    myPlot(x, out, xName='时间(s)', yName='输出信号输出', label='输出信号', figureNum=1, k=2)

main()
