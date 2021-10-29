x = 600851475143

factor = 2
latest_factor = 0
while factor**2 <= x:
    while x % factor == 0:
        latest_factor = factor
        x /= factor
    factor += 1

print(x)
