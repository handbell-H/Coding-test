import sys

n = int(input())
F = list(map(int, input().split()))

lst = []
for i in range(len(F)):
    for j in range(len(F)):
        if i == j or i > j:
            pass
        else:
            lst.append([F[i], F[j]])
lst2 = []
for k in lst:
    lst2.append(k[0]*k[1])
print(max(lst2))
