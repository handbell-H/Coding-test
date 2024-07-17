import sys

N = int(input())

lst2 = []
for n in range(N):

    S, T = input().split()
    S, T = S.upper(), T.upper()
    S_lst, T_lst = list(S), list(T)

    lst = []
    for i in range(len(S_lst)):
        lst.append([S_lst[i], T_lst[i]])

    for j in lst:
        if j[0] == 'X':
            lst2.append(j[1])

print(''.join(lst2))