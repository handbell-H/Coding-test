import sys

a, b, d = map(int, input().split())

if a != d:
    round = (d // a) + (d // b)
    result1 = round * (a + b)
    result2 = (d % a) + (d % b)
    print(result1 + result2)
else:
    round = (d // a) + (d // b)
    result1 = round * (a + b) - b
    result2 = (d % a) + (d % b)
    print(result1 + result2)
