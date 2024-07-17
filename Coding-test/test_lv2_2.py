import sys

N = int(input())
r_lst = list(map(int, input().split()))
max_lst = max(r_lst)

lst_1 = []
for i in range(2, max_lst + 1):
    lst_2 = []
    for j in range(len(r_lst)):
        test = r_lst[j] % i
        lst_2.append(test)
    lst_1.append(lst_2)

lst_3 = []
for k in range(len(lst_1)):
    lst_3.append(lst_1[k].count(0))

print(max(lst_3))