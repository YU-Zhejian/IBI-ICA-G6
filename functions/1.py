#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:46:43 2020

@author: halowin
"""

def gc_calc (DNA:str):
    '''
    Calculating GC content of any user-specified DNA sequence.
    :param DNA:
    :return:
    '''
    import re
    return (str(round(len(re.findall(r'G|C',DNA))/len(DNA)*100,2))+'%')

print(gc_calc('TAGCATCGGCATTACTGAC'))
#47.37%
