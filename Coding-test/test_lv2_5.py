from sys import stdin
import math

K, P, N = map(int, stdin.readline().split())

key = 1e9 + 7
ar = math.pow(P, N)
print(int((K * ar) % key))
