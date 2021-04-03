def getArea(a,b,c):
    return abs((a[0] - c[0])*(b[1] -a[1]) -(a[0]-b[0])*(c[1]-a[1]))

f=open('p102_triangles.txt')
ans=0
for x in f:
    x=list(map(int,x.split(',')))
    a,b,c=((x[0],x[1]),(x[2],x[3]),(x[4],x[5]))
    p=(0,0)
    s=getArea(a,b,p)+getArea(a,p,c)+getArea(p,b,c)
    ss=getArea(a,b,c)
    if ss== s:
        ans+=1

print(ans)