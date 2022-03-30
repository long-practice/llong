# 이차원 배열과 연산

import sys
input = sys.stdin.readline

r, c, k = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(3)]


def calc():
    count_dict = dict()
    M = 0

    for i in range(len(A)):
        for e in A[i]:
            if e:
                count_dict[e] = count_dict.get(e, 0) + 1

        row = []
        for tup in sorted(list(count_dict.items()), key=lambda x: (x[1], x[0])):
            row.extend(list(tup))
            if len(row) == 100:
                break
        A[i] = row[:]
        M = max(M, len(row))
        count_dict.clear()

    for i in range(len(A)):
        for _ in range(M - len(A[i])):
            A[i].append(0)


answer = 0
while answer <= 100:
    if r <= len(A) and c <= len(A[0]) and A[r - 1][c - 1] == k:
        break
    if len(A) >= len(A[0]):
        calc()
    else:
        A = [list(row) for row in list(zip(*A))]
        calc()
        A = [list(row) for row in list(zip(*A))]
    answer += 1
print(answer) if answer <= 100 else print(-1)