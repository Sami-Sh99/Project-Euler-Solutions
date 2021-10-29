f = {}
f[0] = 1
f[1] = 1


def fibo(n):
    if f.get(n, 0) != 0:
        return f[n]
    f[n] = f.get(n-1, 0)+f.get(n-2, 0)
    return f[n]


i = 0
s = 0
while fibo(i) <= 4000000:
    if fibo(i) % 2 == 0:
        s += fibo(i)
    print(i, s, fibo(i))
    i += 1
print(s)
