#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
