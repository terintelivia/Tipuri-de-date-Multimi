A=set(input('Dati litere latine pentru multimea A:'))
B=set(input('Dati litere latine pentru multimea B:'))
y=0
for i in A:
    if ord(i) not in range(65,91):
       y+=1

for i in B:
    if ord(i) not in range(65,91):
        y=+1
if y>0:
    print('Multimile A si B trebuie sa contina litere mari din alfabetul latin')
if y==0:
  print('a) Intersectia multimilor A si B este=',A.intersection(B))
  print('b) Reuniunea multimilor A si B este=',A.union(B))
  print('c) Diferenta multimilor A si B este=',A.difference(B))
  print('c) Diferenta multimilor B si A este=',B.difference(A))