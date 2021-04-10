
def isSimilar(n,m):
    n=list(str(n))
    m=list(str(m))
    if len(n)!=len(m): return False
    for i in n:
        if i not in m:
            return False
    return True

def isValid(n):
    return isSimilar(n,2*n) and isSimilar(n,3*n) and isSimilar(n,4*n) and isSimilar(n,5*n) and isSimilar(n,6*n)

n=1
while True:
    if isValid(n):
        print(n)
        break
    n+=1
    