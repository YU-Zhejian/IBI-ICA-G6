#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gc_calc (DNA:str):
    '''
    Calculating GC content of any user-specified DNA sequence.
    :param DNA:
    :return:
    '''
    import re
    return (str(round(len(re.findall(r'G|C',DNA))/len(DNA)*100,2))+'%')
# demo code:
print(gc_calc('TAGCATCGGCATTACTGAC'))
#47.37%
