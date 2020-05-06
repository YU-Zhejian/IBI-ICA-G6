#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_compl_dna(DNA:str):
    '''
    Compute the complementary DNA strand form any user-specified DNA sequence.
    :param DNA:
    :return:
    '''
    return DNA[::-1].translate(str.maketrans('ATCG', 'TAGC'))
# demo code:
print(get_compl_dna('ATGTTGAATAGTTCAAGAAAATATGCTTGTCGTTCCCTATTCAGACAAGCGATGCGACTACGATCGAGGGCCAT'))
#MQGGESLLSRYHRKVDLLWFLDQDYPRPSN
