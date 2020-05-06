#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mrna2pro(m:str):
    '''
    Protein Translator
    :param m:
    :return:
    '''
    # Corresponding relations between mRNA sequence and amino acid
    table = {
        'UAU':'Y', 'UAC':'Y',
        'UGU':'C', 'UGG':'W', 'UGC':'C',
        'UUG':'L', 'UUA':'L', 'UUU':'F', 'UUC':'F',
        'UCG':'S', 'UCA':'S', 'UCU':'S', 'UCC':'S',
        'GAU':'D', 'GAG':'E', 'GAC':'D', 'GAA':'E',
        'GGU':'G', 'GGG':'G', 'GGC':'G', 'GGA':'G',
        'GUG':'V', 'GUA':'V', 'GUU':'V', 'GUC':'V',
        'GCU':'A', 'GCG':'A', 'GCC':'A', 'GCA':'A',
        'CAU':'H', 'CAG':'Q', 'CAC':'H', 'CAA':'Q',
        'CGU':'R', 'CGG':'R', 'CGC':'R', 'CGA':'R',
        'CUG':'L', 'CUA':'L', 'CUU':'L', 'CUC':'L',
        'CCU':'P', 'CCG':'P', 'CCC':'P', 'CCA':'P',
        'AGU':'S', 'AGG':'R', 'AGC':'S', 'AGA':'R',
        'AAG':'K', 'AAA':'K', 'AAU':'N', 'AAC':'N',
        'AUC':'I', 'AUA':'I', 'AUG':'M', 'AUU':'I',
        'ACC':'W', 'ACU':'W', 'ACG':'W', 'ACA':'W'
    }
    #The sequence of the amino acid
    proteinsequence= ''
    start = m.find('AUG')
    # Three codons correspond to one amino acid
    for n in range(start,len(m),3):
        if m[n:n + 3] in table.keys():
            print(m[n:n + 3]+"->"+table[m[n:n + 3]])
            #add the translated amino acid to the polypeptide sequence
            proteinsequence += table[m[n:n + 3]]
        else:
            break
    return(proteinsequence)
# demo code:
print(mrna2pro('AUGCAGGGUGGUGAAUCGUUGUUAUCUCGUUACCACCGGAAGGUAGACCUUUUAACUUUUUUGGACCAAGAUUAUCCGAGACCAAGUAACUAA'))
#MQGGESLLSRYHRKVDLLWFLDQDYPRPSN
