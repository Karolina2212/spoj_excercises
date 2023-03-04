# https://pl.spoj.com/problems/VSR/

t = int(input())
for i in range(t):
    n = input()
    v_tab = list(map(int, n.split(" ")))
    v_average = (2*v_tab[0]*v_tab[1])/(v_tab[0]+v_tab[1])
    print(int(v_average))