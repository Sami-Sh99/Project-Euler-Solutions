def validate(n):
    n=n**2
    l=list(str(n))
    v=[1,'_',2,'_',3,'_',4,'_',5,'_',6,'_',7,'_',8,'_',9,'_',0]
    if(len(l))>19:
        return False
    for i in range(0,19,2):
        if not type(v[i])==str and int(l[i])!=v[i]:
            return False
    return True

for i in range(1010101010,1389026623,10):
    if validate(i):
        print(i)
        break
print("done")

