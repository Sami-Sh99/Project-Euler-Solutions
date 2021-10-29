limit=1000000

count =0

outer=3
while True:
    sum=0
    inner=outer
    while inner>=3:
        ring=4*(inner-1)
        if(sum+ring>limit):break
        sum+=ring
        count+=1
        inner-=2
    if(sum==0):break
    outer+=1

print(count)