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
