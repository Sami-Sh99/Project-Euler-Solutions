
class State:
    red=0
    blue=0
    possibilities=0
    def __init__(self,r,b,p):
        self.red=r
        self.blue=b
        self.possibilities=p


Open=[State(0,0,1)]
possiblities=1
avRed=1
avBlue=1
maxRounds=5
for i in range(1,maxRounds+1):
    possiblities*=avRed+avBlue
    n=list()
    for j in range(i):
        s=State(i-j,j,0)
        n.append(s)
    for o in range(len(Open)):
        n[Open[o].blue-1].possibilities+=Open[o].possibilities* avRed
        n[Open[o].blue].possibilities+=Open[o].possibilities* avBlue
    Open=n
    avRed+=1

moreBlue=0
for cur in Open:
    if cur.blue>cur.red:
        moreBlue+=cur.possibilities

print(possiblities/moreBlue)