# N-Queen
# https://www.acmicpc.net/problem/9663
# https://programmers.co.kr/learn/courses/30/lessons/12952

# 시간이 과도하게 소모되는 경향이 있음
N = int(input())

array = [20 for _ in range(N)]
answer = 0

def check(row):
    for j in range(row):
        if array[row] == array[j] or row - j == abs(array[row] - array[j]):
            return False
    return True

def searching(row, recur_count):
    global answer
    if recur_count == N:
        answer += 1
        return
    else:
        for i in range(len(array)):
            array[row] = i
            if check(row):
                searching(row + 1, recur_count + 1)
            array[row] = 20

searching(0, 0)
print(answer)