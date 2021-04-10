perm=[1,2,3,4,5,6,7,8,9]

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

def CheckPartitions(startIndex, prev) :
    count = 0
    for  i in range(startIndex,len(perm)):
        number = 0
        for j in range(startIndex, i+1):
            number = number * 10 + perm[j];                    
        
        if(number < prev) : continue

        if( not isPrime(number)) : continue

        if(i == (len(perm)-1)): return count + 1
        
        count += CheckPartitions(i + 1, number)
    return count

def isPrime(n) :
	if (n <= 1) :
		return False
	if (n <= 3) :
		return True
	if (n % 2 == 0 or n % 3 == 0) :
		return False
	i = 5
	while(i * i <= n) :
		if (n % i == 0 or n % (i + 2) == 0) :
			return False
		i = i + 6
	return True
cnt=0

c=CheckPartitions(0,0)

while(nextPermuation()):
    c+=CheckPartitions(0,0)

print(c)