import itertools
A={1,2,3,4}
for i in range(len(A)):
    submultimi=itertools.combinations(A ,i+1)
    print('Submultimile multimii A sunt:',set(submultimi))
