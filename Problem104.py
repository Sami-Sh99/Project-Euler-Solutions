
def Check(n):
    n=list(str(n))
    s=n[:10]
    if len(n)<18:return False
    if '1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s and '9' in s:
        s=n[-9:]
        if '1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s and '9' in s:
            return True
    return False



n=1
fn=1
x = 0
y = 1
while(True):
        z = (x + y)
        x = y
        y = z
        fn=z
        n+=1
        if Check(fn):break

# print(fn)
print(n)