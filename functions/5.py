#!/usr/bin/env python3
# -*- coding: utf-8 -*-

se=[]

def dna2rna(DNA:str):
    return(DNA.translate(str.maketrans("AGCT","UCGA")))

def dna_compl(dna:str) -> str:
    return(dna[::-1].translate(str.maketrans("AGCT", "TCGA")))

def pp_calc_sub(dna:str) -> int:
    global se
    ends=["UAG","UAA","UGA"]
    begins=["AUG"]
    reading = False
    counter = 0
    rna=dna2rna(dna)
    idx=0
    se=[]
    se_tmp=[None,None]
    for i in range(len(dna)-2):
        curr3=rna[i:i+3]
        if reading:
            idx+=1
            if idx%3!=0:
                continue
            if ends.count(curr3):
                counter=counter+1
                reading=False
                se_tmp[1]=i+3
                se.append(se_tmp.copy())
                idx=0
        else:
            if begins.count(curr3):
                reading=True
                se_tmp[0]=i
    return(counter)

def print_se(dna:str):
    global se
    i=0
    for se_tmp in se:
        i+=1
        print("No. "+str(i)+": "+str(se_tmp[0])+"-->"+str(se_tmp[1])+", len: "+ str(((se_tmp[1]-se_tmp[0]))//3))
        print(dna[se_tmp[0]:se_tmp[1]])

def pp_calc(dna:str):
    '''
    Compute the number of polypeptides produced by any user-specified DNA sequence.
    :param dna:
    :return:
    '''
    print("Input DNA get "+str(pp_calc_sub(dna))+" polypipetides.")
    print_se(dna)
    print("Completemeentary DNA get "+str(pp_calc_sub(dna_compl(dna)))+" polypipetides.")
    print_se(dna_compl(dna))
# demo code:
pp_calc("""ATGTTGAATAGTTCAAGAAAATATGCTTGTCGTTCCCTATTCAGACAAGCGAACGTCTCAATAAAAGGACTCTTTTATAATGGAGGCGCATATCGAAGAGGGTTTTCAACGGGATGTTGTTTGAGGAGTGATAACAAGGAAAGCCCAAGTGCAAGACAACCACTAGATAGGCTACAACTAGGTGATGAAATCAATGAACCAGAGCCTATTAGAACCAGGTTTTTTCAATTTTCCAGATGGAAGGCCACCATTGCTCTATTGTTGCTAAGTGGTGGGACGTATGCCTATTTATCAAGAAAAAGACGCTTGCTAGAAACTGAAAAGGAAGCAGATGCTAACAGAGCTTACGGTTCAGTAGCACTTGGCGGTCCTTTCAATTTAACAGATTTTAATGGTAAGCCTTTCACTGAGGAGAATTTGAAGGGTAAGTTTTCCATTTTATACT""")
#Input DNA get 2 polypipetides.
#No. 1: 172-->289, len: 39
#TACAACTAGGTGATGAAATCAATGAACCAGAGCCTATTAGAACCAGGTTTTTTCAATTTTCCAGATGGAAGGCCACCATTGCTCTATTGTTGCTAAGTGGTGGGACGTATGCCTATT
#No. 2: 345-->408, len: 21
#TACGGTTCAGTAGCACTTGGCGGTCCTTTCAATTTAACAGATTTTAATGGTAAGCCTTTCACT
#Completemeentary DNA get 1 polypipetides.
#No. 1: 18-->210, len: 64
#TACCCTTCAAATTCTCCTCAGTGAAAGGCTTACCATTAAAATCTGTTAAATTGAAAGGACCGCCAAGTGCTACTGAACCGTAAGCTCTGTTAGCATCTGCTTCCTTTTCAGTTTCTAGCAAGCGTCTTTTTCTTGATAAATAGGCATACGTCCCACCACTTAGCAACAATAGAGCAATGGTGGCCTTCCATC
