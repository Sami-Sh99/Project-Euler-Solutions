def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime


n=100
primes=SieveOfEratosthenes(n)
primes=[i for i in range(len(primes)) if primes[i]]

primeSum=[0]
for i in range(len(primes)):
    primeSum.append(primeSum[i]+primes[i])


s=0

print(s)