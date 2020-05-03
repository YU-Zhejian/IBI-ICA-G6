#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_compl_dna(DNA:str):
    '''
    Compute the complementary DNA strand form any user-specified DNA sequence.
    :param DNA:
    :return:
    '''
    compl_dict = str.maketrans('ATCG', 'TAGC')
    res = list(DNA.translate(compl_dict))
    res.reverse()
    return (''.join(res))

print(get_compl_dna('ATGCGACTACGATCGAGGGCCAT'))
#ATGGCCCTCGATCGTAGTCGCAT
