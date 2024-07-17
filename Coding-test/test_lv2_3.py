import sys

arr = [list(map(int,input().split())) for _ in range(3)]

arr_tran = []
for i in range(len(arr)):
    lst_2 = []
    for j in range(len(arr)):
        lst_2.append(arr[j][i])
    arr_tran.append(lst_2)

res_lst = []
for j in range(len(arr)):
    a,b,c = arr[j]
    if a == b == c:
        res = 0
    elif max(arr[j]) - min(arr[j]) == 1:
        res = 1
    else:
        res = 2
    res_lst.append(res)

for k in range(len(arr_tran)):
    d,e,f = arr_tran[k]
    if d == e == f:
        res = 0
    elif max(arr_tran[j]) - min(arr_tran[j]) == 1:
        res = 1
    else:
        res = 2
    res_lst.append(res)

'''
# 입력 받기
arr = [list(map(int, input().split())) for _ in range(3)]

# 행렬 전치
arr_tran = list(zip(*arr))

# 결과 계산 함수
def calculate_result(line):
    if line[0] == line[1] == line[2]:
        return 0
    elif max(line) - min(line) == 1:
        return 1
    else:
        return 2

# 각 행과 열에 대해 결과 계산
res_lst = [calculate_result(row) for row in arr] + [calculate_result(col) for col in arr_tran]

# 최소값 출력
print(min(res_lst))
'''

print(min(res_lst))
