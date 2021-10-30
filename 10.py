def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime


x = SieveOfEratosthenes(int(2e6))

s = 0
for ix, k in enumerate(x):
    if k:
        s += ix
print(s)
