# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:31:00 2023

@author: YXD
"""

import numpy as np
class CLASS_FILTER:
    N = 0
    length = 0
    c = np.zeros(100)
    def init(self, N):
        self.N = N
    def calc(self, u):
        self.init(5)
        self.length += 1
        self.c[self.length - 1] = u
        sum = 0
        
        if(self.length < self.N):
            for i in range(self.length):
                sum += self.c[i]
            for i in range(self.N - self.length):
                sum += self.c[0]
        else:
            for i in range(self.length - self.N, self.length):
                sum += self.c[i]
        return sum / self.N

myFilter = CLASS_FILTER()

a = [1,24,34,6,45,76,7,43.4,5,6,7,86,4,5,6]
length = len(a)
b = np.zeros(length)
for i in range(length):
    b[i] = myFilter.calc(a[i])


print(b)

