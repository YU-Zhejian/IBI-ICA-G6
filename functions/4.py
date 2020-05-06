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
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGG':'R', 'AGA':'R',
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'CCC':'P', 'CCA':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGC':'R', 'CGU':'R', 'CGA':'R', 'CGG':'R',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'GCA':'A', 'GCU':'A', 'GCC':'A', 'GCG':'A',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGA':'G', 'GGC':'G', 'GGG':'G',
    'UCA':'S', 'UCG':'S', 'UCC':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUG':'L', 'UUA':'L',
    'UAU':'Y', 'UAC':'Y', 'UGU':'C', 'UGC':'C',
    'UGG':'W', 
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
