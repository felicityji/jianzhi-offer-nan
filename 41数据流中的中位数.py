#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:52:30 2019

@author: felicity
"""

class Solution:
    def __init__(self):
        self.nums = []
    def Insert(self, num):
        self.nums.append(num)
    def GetMedian(self, fuck):
        self.nums.sort()
        if len(self.nums) % 2 == 1:
            return self.nums[(len(self.nums) - 1) / 2]
        else:
            return (self.nums[len(self.nums) / 2] + self.nums[len(self.nums) / 2 - 1]) / 2.0
--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/79725893 
版权声明：本文为博主原创文章，转载请附上博文链接！