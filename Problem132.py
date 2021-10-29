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
s = set()
n, L = 5, 10**9

while len(s) < 40:
    if isPrime(n) and pow(10, L, n) == 1: s.add(n)
    n += 2

print(sum(s))