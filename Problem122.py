cost=[10000000]*201
path = [0]*200
limit=201

def Backtrack(power, depth) :
    if (power >= limit or depth > cost[power]) : return
    cost[power] = depth
    path[depth] = power
    for i in range(depth,-1,-1):
        Backtrack(power + path[i], depth + 1)

Backtrack(1,0)
print(sum(cost[1:]))