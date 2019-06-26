#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:58:38 2019

@author: dongdong
"""

from abc import ABCMeta, abstractmethod, abstractproperty
class DataSet(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def Update(self,ind):
        pass
    
    @abstractmethod
    def GetLatestInd(self,N = 1):
        pass
    
    @abstractmethod
    def ComeToEnd(self,ind):
        pass   
    @abstractmethod
    def GetLatestPrice(self,code):
        pass  
    
class HistToryDataSet(DataSet):
    def __init__(self):
        self.ind_list = [1,2,3,4]
        self.data = {}
        
    def Update(self,ind):
        return ind + 1
    def ComeToEnd(self,ind):
        if ind == self.ind_list[-1]:
            return True
        return False
    def GetLatestInd(self,N = 1):
        return self.ind_list[-1]   
    def GetLatestPrice(self,code):
        return 1.0
    
    
    
class RealTimeDataSet(DataSet):
    def __init__(self):
        pass
    def Update(self,ind):
        self.data = self.GetNewData()
        return ind
    def ComeToEnd(self,ind):
        timenow = '15:00'
        if timenow:
            return False
def CreateHistoryDataSet():
    return HistToryDataSet()