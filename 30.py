upper_bound = 7*9**5

ans = 0
for i in range(2, upper_bound):
    k = list(str(i))
    s = 0
    for j in k:
        s += int(j)**5
    if s == i:
        ans += i

print(ans)
