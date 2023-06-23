# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:31:00 2023

@author: YXD
"""

import numpy as np
class CLASS_FILTER:
    N = 0
    FC = 0
    length = 0
    c = np.zeros(100)
    def init(self, FC, N):
        self.N = N
        self.FC = FC
    def calc(self, u):
        self.length += 1
        self.c[self.length - 1] = u
        sum = 0
        
        if(self.length < self.N):
            for i in range(self.length):
                sum += self.c[i] * self.FC[self.length - 1 - i]
            for i in range(self.N - self.length):
                sum += self.c[0] * self.FC[self.N - 1 - i]
        else:
            for i in range(self.length - self.N, self.length):
                sum += self.c[i] * self.FC[self.length - 1 - i]
        return sum

myFilter = CLASS_FILTER()
u = [1,24,34,6,45,76,7,43.4,5,6,7,86,4,5,6]
filterCoeff = [0.2, 0.2, 0.2, 0.2, 0.2]
filterN = len(filterCoeff)
length = len(u)
y = np.zeros(length)
myFilter.init(filterCoeff, filterN)
for i in range(length):
    y[i] = myFilter.calc(u[i])


print(y)

