import sys

W, N = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]

info.sort(key=lambda x: x[1], reverse=True)

res = 0
for weight, price in info:
    if W - weight >= 0 :
        res += weight * price
        W -= weight
    else:
        res += W * price
        break;
print(res)