#!/usr/bin/env python
# This python code encloses a function which can compute the number of polypeptides produced by a user-specified DNA.S

se=[]
def dna_compl(dna:str) -> str:
    dna_rev = dna[::-1]
    return(dna_rev.translate(str.maketrans("AGCT", "TCGA")))

def dna2rna(dna:str) -> str:
    dna_rev = dna[::-1]
    return(dna_rev.translate(str.maketrans("AGCT", "UCGA")))

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
                se_tmp[1]=i
                se.append(se_tmp.copy())
                idx=0
        else:
            if begins.count(curr3):
                reading=True
                se_tmp[0]=i
    return(counter)

def print_se():
    global se
    i=0
    for se_tmp in se:
        i+=1
        print("No. "+str(i)+": "+str(se_tmp[0])+"-->"+str(se_tmp[1])+", len: "+ str(((se_tmp[1]-se_tmp[0]))//3))

def pp_calc(dna:str):
    print("Input DNA get "+str(pp_calc_sub(dna))+" polypipetides.")
    print_se()
    print("Completemeentary DNA get "+str(pp_calc_sub(dna_compl(dna)))+" polypipetides.")
    print_se()

pp_calc("""ATGTTGAATAGTTCAAGAAAATATGCTTGTCGTTCCCTATTCAGACAAGCGAACGTCTCAATAAAAGGACTCTTTTATAATGGAGGCGCATATCGAAGAGGGTTTTCAACGGGATGTTGTTTGAGGAGTGATAACAAGGAAAGCCCAAGTGCAAGACAACCACTAGATAGGCTACAACTAGGTGATGAAATCAATGAACCAGAGCCTATTAGAACCAGGTTTTTTCAATTTTCCAGATGGAAGGCCACCATTGCTCTATTGTTGCTAAGTGGTGGGACGTATGCCTATTTATCAAGAAAAAGACGCTTGCTAGAAACTGAAAAGGAAGCAGATGCTAACAGAGCTTACGGTTCAGTAGCACTTGGCGGTCCTTTCAATTTAACAGATTTTAATGGTAAGCCTTTCACTGAGGAGAATTTGAAGGGTAAGTTTTCCATTTTATACTTTGGATTCAGTCATTGCCCCGACATTTGTCCAGAAGAGCTTGACAGATTAACGTATTGGATTTCTGAATTAGATGATAAAGACCATATAAAGATACAGCCATTGTTTATCTCATGTGATCCTGCAAGAGATACACCGGATGTCTTGAAAGAGTACTTAAGCGATTTTCACCCAGCTATCATTGGTTTAACCGGTACGTACGACCAAGTGAAAAGCGTATGCAAAAAATACAAGGTATATTTTTCAACTCCACGTGATGTCAAGCCCAACCAGGATTACTTAGTGGACCATTCGATATTTTTCTATTTGATCGACCCTGAAGGACAGTTTATCGATGCGTTGGGAAGAAACTACGATGAGCAATCTGGTCTCGAAAAGATTCGTGAACAAATTCAGGCGTATGTGCCAAAGGAAGAACGGGAGCGTAGGTCAAAAAAATGGTACTCTTTTATCTTC""")
