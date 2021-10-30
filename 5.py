def gcd(a, b):
    while(a != 0):
        c = a
        a = b % a
        b = c
    return b


def lcm(a, b):
    return a*(b/gcd(a, b))


a = 1
for i in range(1, 21):
    a = int(lcm(a, i))
print(a)
