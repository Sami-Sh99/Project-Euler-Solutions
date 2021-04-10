perm=[0,1,2,3,4,5,6,7,8,9]

def nextPermuation() :

    N = len(perm)
    i = N - 1

    while (perm[i - 1] >= perm[i]) :
        i = i - 1
        if (i == 0):return False

    j = N
    while (perm[j - 1] <= perm[i - 1]): j = j - 1

    swap(i - 1, j - 1)

    i+=1
    j = N

    while (i < j) :
        swap(i - 1, j - 1)
        i+=1
        j-=1

    return True

def swap(i,j) :
    k = perm[i]
    perm[i] = perm[j]
    perm[j] = k

for i in range(1,1000000):
    nextPermuation()

print(''.join(list(map(str,perm))))