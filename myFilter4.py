import numpy as np
class CLASS_FILTER:
    def init(self, FilterCoeff, N):
        self.index = 0                                                          #缓冲区索引
        self.M = N + 1                                                          #N为滤波器阶数，self.M为滤波器系数个数
        self.buff = np.zeros(self.M)                                            #滤波器输入的数据闭环缓冲区，即该缓冲区索引达到最后时，下一次索引移动操作(索引每次加一)会将索引置0
        self.FilterCoeff = FilterCoeff                                          #滤波器系数序列
        self.first = True                                                       #第一个输入数据处理的标志
        self.a = 0                                                              #存储偏置，即存储第一个输入数据
        
    def calc(self, u):
        if(self.first):
            self.a = u
            self.first = False
        def index(i):
            return (self.index + i + self.M) % self.M
        self.buff[self.index] = u - self.a
        sum = 0
        
        for i in range(self.M):
            sum += self.buff[index(-i)] * self.FilterCoeff[i]
                
        self.index = (self.index + 1) % self.M
        return sum + self.a

def main():
    myFilter = CLASS_FILTER()
    u = [1,24,34,6,45,76,7,43.4,5,6,7,86,4,5,6]
    filterCoeff = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
    filterN = len(filterCoeff) - 1
    length = len(u)
    y = np.zeros(length)
    myFilter.init(filterCoeff, filterN)
    for i in range(length):
        y[i] = myFilter.calc(u[i])
    print(y)

main()
