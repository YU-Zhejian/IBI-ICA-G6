m=input("Write mRNA sequence here:")
sequence=list(m)
# Corresponding relations between mRNA sequence and amino acid
table = {
    'UAU':'I', 'UAG':'I', 'UAA':'I', 'UAC':'M',
    'UGU':'T', 'UGG':'T', 'UGC':'T', 'UGA':'T',
    'UUG':'N', 'UUA':'N', 'UUU':'K', 'UUC':'K',
    'UCG':'S', 'UCA':'S', 'UCU':'R', 'UCC':'R',
    'GAU':'L', 'GAG':'L', 'GAC':'L', 'GAA':'L',
    'GGU':'P', 'GGG':'P', 'GGC':'P', 'GGA':'P',
    'GUG':'H', 'GUA':'H', 'GUU':'Q', 'GUC':'Q',
    'GCU':'R', 'GCG':'R', 'GCC':'R', 'GCA':'R',
    'CAU':'V', 'CAG':'V', 'CAC':'V', 'CAA':'V',
    'CGU':'A', 'CGG':'A', 'CGC':'A', 'CGA':'A',
    'CUG':'D', 'CUA':'D', 'CUU':'E', 'CUC':'E',
    'CCU':'G', 'CCG':'G', 'CCC':'G', 'CCA':'G',
    'AGU':'S', 'AGG':'S', 'AGC':'S', 'AGA':'S',
    'AAG':'F', 'AAA':'F', 'AAU':'L', 'AAC':'L',
    'AUG':'Y', 'AUA':'Y', 'ACG':'C', 'ACA':'C',
    'ACC':'W',
}
#The sequence of the amino acid
proteinsequence= ''
start = sequence.find('UAC')
sequencestart = sequence[int(start):]
# Three codons correspond to one amino acid
for n in range(0, len(sequence)):
    if sequence[n:n + 3] in table.keys():
        #add the translated amino acid to the polypeptide sequence
        proteinsequence += table[sequence[n:n + 3]]
    else:
        break
print(proteinsequence)