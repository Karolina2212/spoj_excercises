# https://pl.spoj.com/problems/FCTRL3/

t = int(input())
for i in range(t):
    n = int(input())
    x = 1
    factorial = 1
    while x<=n:
        factorial = factorial*x
    # when 2 last num are 0s - for all following multiplications 2 last num will remain 0s:
        if factorial % 100 == 0:
            break
        x+=1
    f = str(factorial)
    if factorial < 10:
        print("0 "+f[-1])
    else:
        print(f[-2]+" "+f[-1])
