

def gen_palindrome(x):
    xs = str(x)
    xs += xs[::-1]
    return int(xs)


max = 10**6
for i in range(999, 99, -1):
    palindrome = gen_palindrome(i)
    j = 100
    while j**2 <= palindrome:
        if palindrome % j == 0:
            k = palindrome/j
            if k >= 100 and k <= 999:
                print(palindrome)
                exit()
        j += 1
