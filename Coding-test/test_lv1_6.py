import sys

lst=[]
for i in range(5):
    start, end = input().split()
    start_h, start_m = start.split(':')
    end_h, end_m = end.split(':')

    start_h, start_m, end_h, end_m = int(start_h), int(start_m), int(end_h), int(end_m)

    if end_m - start_m >= 0:
        result = (end_h - start_h) * 60 + (end_m - start_m)
    else:
        result = (end_h - start_h - 1) * 60 + (end_m + (60 - start_m))
    lst.append(result)

print(sum(lst))
