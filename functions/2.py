seq = 'ATGCGACTACGATCGAGGGCCAT'
compl_dict = str.maketrans('ATCG', 'TAGC')
res = list(seq.translate(compl_dict))
res.reverse()
print(''.join(res))
