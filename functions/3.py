#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:22:07 2020

@author: jacka
"""

def dna2rna(DNA:str):
    '''
    Compute the mRNA sequence form any user-specified DNA sequence.
    :param DNA:
    :return:
    '''
    return(DNA.translate(str.maketrans("AGCT","UCGA")))
# demo code:
print(dna2rna('ATGCGACTACGATCGAGGGCCAT'))
#UACGCUGAUGCUAGCUCCCGGUA
