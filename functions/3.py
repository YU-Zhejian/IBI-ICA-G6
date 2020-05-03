# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:22:07 2020

@author: jacka
"""
def Convertor(s:str):
    c= ''
    for i in range(0,s):
       if DNA[i] == 'A':
          c = 'T' +c
       elif DNA[i] == 'T':
          c = 'A' +c
       elif DNA[i] == 'G':
          c = 'C' +c
       elif DNA[i] == 'C':
          c = 'G' +c
    return (c)
