#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 01:37:06 2019

@author: felicity
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        if self.GetLastK(data, k) == -1 and self.GetFirstK(data, k) == -1:
            return 0
        return self.GetLastK(data, k) - self.GetFirstK(data, k) + 1
        
    def GetFirstK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                if mid == low or data[mid - 1] != k: #当到list[0]或不为k的时候跳出函数
                    return mid
                else:
                    high = mid - 1
        return -1

    def GetLastK(self, data, k): #找到k时即data[mid] = k ，判断当前位置是否时最后一个数字或者后一个是否等于k，若等于k并且当前位置不是最后一个位置，则low=mid+1,目的是在mid（当前）的后一段再重新找k，重复上面的逻辑，直到找到最后一个k为止并返回当前k的位置
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:   #data[mid] = k 
                if mid == high or data[mid + 1] != k: #mid = high已经找到最后一个数字时，返回mid。或者在当前mid后一个数字不等于k时，返回mid
                    return mid
                else:   #这里就是 data[mid + 1] = k && mid != high  这时需要去到mid后面一段找k
                    low = mid + 1
        return -1
