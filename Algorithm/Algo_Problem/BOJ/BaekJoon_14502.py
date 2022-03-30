# 연구소
# func_1 0 field 찾기(기둥을 놓을 수 있는 공간이 어디인지)
# func_2 벽 세우기
# func_3 바이러스 퍼트리기
# func_4 남은 칸 세기

import copy
from collections import deque

def func_1(arr, N, M):
    zero, virus = [], []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                zero.append((r, c))
            elif arr[r][c] == 2:
                virus.append((r, c))
    return zero, virus

def func_2(arr, zeros):
    for _ in range(3):
        r, c = zeros.pop()
        arr[r][c] = 1

def dfs(arr, row, col):
    if row - 1 >= 0 and arr[row - 1][col] == 0:
        arr[row - 1][col] = 2
        dfs(arr, row - 1, col)
    if row + 1 <= N - 1 and arr[row + 1][col] == 0:
        arr[row + 1][col] = 2
        dfs(arr, row + 1, col)
    if col - 1 >= 0 and arr[row][col - 1] == 0:
        arr[row][col - 1] = 2
        dfs(arr, row, col - 1)
    if col + 1 <= M - 1 and arr[row][col + 1] == 0:
        arr[row][col + 1] = 2
        dfs(arr, row, col + 1)

def func_3(arr, N, M):
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 2:
                dfs(arr, r, c)

def bfs(arr, virus):
    queue = deque(virus)

    while queue:
        row, col = queue.popleft()

        if row - 1 >= 0 and arr[row - 1][col] == 0:
            arr[row - 1][col] = 2
            queue.append((row - 1, col))
        if row + 1 <= N - 1 and arr[row + 1][col] == 0:
            arr[row + 1][col] = 2
            queue.append((row + 1, col))
        if col - 1 >= 0 and arr[row][col - 1] == 0:
            arr[row][col - 1] = 2
            queue.append((row, col - 1))
        if col + 1 <= M - 1 and arr[row][col + 1] == 0:
            arr[row][col + 1] = 2
            queue.append((row, col + 1))

def func_4(arr, N, M):
    count = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                count += 1
    return count

N, M = map(int, input().split(' '))
array = [list(map(int, input().split(' '))) for _ in range(N)]
answer = set()

zero_fields, virus_fields = func_1(array, N, M)

# zero field 3개 선택하기
for z1 in range(len(zero_fields) - 2):
    for z2 in range(z1 + 1, len(zero_fields) - 1):
        for z3 in range(z2 + 1, len(zero_fields)):
            array_temp = copy.deepcopy(array)
            # func_2: zero field 3군데를 1로 도핑
            func_2(array_temp, [zero_fields[z1], zero_fields[z2], zero_fields[z3]])
            # func_3: field 값이 2인 곳에 dfs시작, 바이러스 퍼트리기
            # func_3(array_temp, N, M)
            # bfs로 바이러스 퍼뜨리기
            bfs(array_temp, virus_fields)
            # func_4: field 값이 0인 곳을 찾기
            # 기둥을 놓을 수 있는 경우에 따라 0의 개수는 다르므로 모든 값들을 answer에 저장
            answer.add(func_4(array_temp, N, M))
# 최댓값 구해내기
print(max(answer))