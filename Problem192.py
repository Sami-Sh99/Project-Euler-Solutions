import math
import numpy as np
n=int(1e5)
tol=1e12
def bisectionFrey(n):
    a,b,c,d=0,1,1,1
    while b<=tol and d<=tol:
        mid=float((a+c)/(b+d))
        if mid<n:
            a=a+c
            b=b+d
        elif mid>n:
            c=a+c
            d=b+d
        else:
            if b+d<tol:
                return a+c,b+d
            elif d<b:
                return c,d
            else:
                return a,b
    if abs(n - c/d) < abs(n - a/b):
        return c, d
    else:
        return a, b
def AllowHalf(a, k) :
    i = k; 
    s = 1
    while (i > 0) :
        difference = s * (a[i] - a[2 * k - i])
        if (difference > 0) :
            return True
        if (difference < 0) :
            return False
        s *= -1
        i-=1
    return ((k - 1) & 1) != 0

def ContinuedFractionRoot(n,number):
        result = [0]*number
        lowsqr = (int) (0.5 + math.sqrt(float(n) ))
        if (lowsqr * lowsqr > n) :
            lowsqr-=1
		
        a0 = 0;b0 = 1

        for i in range(0,number):
            f1 = (a0 + lowsqr) // b0
            a1 = b0 * f1 - a0
            b1 = (n - a1 * a1) // b0
            result[i] = f1
            a0 = a1
            b0 = b1

        return result


def LowestDenominator(a, limit):
    n2 = 1; d2 = 0
    n1 = a[0]; d1 = 1
    i = 1
    while (True) :
        n = 0; d = 0
        minval = ((a[i] + 1) // 2)
        if ((a[i] & 1) == 0 and not AllowHalf(a, i)) :
            minval+=1
        for q in range(minval,a[i]+1):
            n = n2 + q * n1
            d = d2 + q * d1
            if (d > limit):
                if (q > minval) :
                    return d2 + (q - 1) * d1
                else :
                    return d1
        n2 = n1
        d2 = d1
        n1 = n
        d1 = d
        i+=1
s=0
for i in range(2,n+1):
    nn=math.sqrt(i)
    if int(nn)**2==i: continue
    s+=LowestDenominator(ContinuedFractionRoot(i, 128),10**12)
print(s)


# x= math.sqrt(13)
# x=x-int(x)
# print(bisectionFrey(x))
    