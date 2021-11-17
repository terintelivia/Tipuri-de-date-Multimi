import itertools
A={'A','B','C','D'}
for i in range(len(A)):
    submultimi=itertools.combinations(A ,i+1)
    print('Submultimile multimii A sunt:',set(submultimi))