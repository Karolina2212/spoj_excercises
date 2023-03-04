# https://pl.spoj.com/problems/RNO_DOD/

t = int(input())
for i in range(t):
    n = int(input())
    n2 = map(int, input().split(" "))
    print(sum(n2))

