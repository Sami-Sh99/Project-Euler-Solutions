
lookup=dict()


def RecPrize(length,Ls,As):
    if Ls==2:return 0
    if As==3: return 0
    if length==0: 
        return 1
    h=length*6+As*2+Ls
    if h in lookup: return lookup[h]
    lookup[h]=RecPrize(length-1,Ls,0)+RecPrize(length-1,Ls+1,0)+RecPrize(length-1,Ls,As+1)
    return lookup[h]


print(RecPrize(30,0,0))

print(1)