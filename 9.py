for i in range(1, int(1000/3)):
    for j in range(i, int(1000/2)):
        k = 1000-i-j
        if i**2+j**2 == k**2:
            a = i*j*k
            print(a)
            exit()
