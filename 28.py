n = 1001


sum = 1
d1 = 1
d2 = 1
for depth in range(1, (n+1)//2):
    d2 = d1+2*depth
    d1 = d1+8*depth
    d3 = d2+2*depth
    d4 = d3+2*depth
    sum += d1+d2+d3+d4

print(sum)
