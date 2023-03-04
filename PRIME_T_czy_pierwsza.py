# https://pl.spoj.com/problems/PRIME_T/

# WERSJA 1

# import math
#
# t = int(input())
# for i in range(t):
#     n = int(input())
#     check = "TAK"
#     if n == 1:
#         print("NIE")
#     else:
#         for x in range(2,round(math.sqrt(n))+1):
#             if n%x == 0:
#                 check = "NIE"
#                 break
#         print(check)

# WERSJA 2 - sito Arystotelesa

list_true = [True] * 10001
list_true[0] = False
list_true[1] = False
for i in range(2, len(list_true)):
    if list_true[i]:
        for j in range(i * 2, len(list_true), i):
            list_true[j] = False
t = int(input())
for test in range(t):
    x = int(input())
    if list_true[x]:
        print("TAK")
    else:
        print("NIE")
