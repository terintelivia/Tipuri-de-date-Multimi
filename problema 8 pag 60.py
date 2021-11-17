A=set(map(int, input("Dati numere intregi pentru multimea A:").split()))
B=set(map(int, input("Dati numere intregi pentru multimea B:").split()))
print('a) Intersectia multimilor A si B este=',A.intersection(B))
print('b) Reuniunea multimilor A si B este=',A.union(B))
print('c) Diferenta multimilor A si B este=',A.difference(B))
print('c) Diferenta multimilor B si A este=',B.difference(A))

