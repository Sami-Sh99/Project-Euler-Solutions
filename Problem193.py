from math import sqrt
import numpy as np
limit=2e50

root=int(sqrt(limit))
print(root)
numPrimeFactors=np.zeros(int(root))

ignore=np.array(int(root),False)

for prime in range(2,root):
    if numPrimeFactors[prime]!=0:
        continue
    for j in range(prime,root,prime):
        numPrimeFactors[j]+=1
    square=prime**2
    for j in range(square,root,square):
        ignore[j]=True

notSquareFree=0
for base in range(2,root):
    if ignore[base]: continue
    square=base**2
    numMultiples=limit/square
    if numPrimeFactors[base]%2==1: notSquareFree+=numMultiples
    else: notSquareFree-=numMultiples

print(limit-notSquareFree)