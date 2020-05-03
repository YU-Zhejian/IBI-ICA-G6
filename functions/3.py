# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:22:07 2020

@author: jacka
"""
def Convertor(s:str):
    return(s.translate(str.maketrans("AGCT","TCGA")))
