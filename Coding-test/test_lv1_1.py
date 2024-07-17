import sys

N = int(input())
rw = []
for i in range(N):
    rw.append([])
    x, y = map(int, input().split())
    rw[i].append(x)
    rw[i].append(y)

lst = []
for i in rw:
    lst.append(i[1])
result = rw.pop(lst.index(min(lst)))
print(*result)
