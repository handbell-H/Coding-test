import sys

n = int(input())
town = list(map(int, input().split()))

lst = []
for i in range(len(town)-1):
    lst.append([town[i], town[i+1]])

lst2 = []
for i in lst:
    distance = i[1] - i[0]
    lst2.append(distance)
min_distance = min(lst2)

lst3 = []
for i in lst2:
    if i == min_distance:
        lst3.append(i)

print(len(lst3))
