cache=[0]*100

def F(m, n) :
 
    solutions = 1
    if (n > m) :return solutions
 
    if (cache[m] != 0): return cache[m]
 
    for startpos in range(0,m-n+1):
        for  blocklength in range(n,m-startpos+1):
            solutions += F(m - startpos - blocklength-1, n)
 
    cache[m] = solutions
    return solutions


print(F(50,3))