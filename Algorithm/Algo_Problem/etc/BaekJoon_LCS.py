# LCS

# 9252번
# 최장 공통 부분 수열(LCS)
# 역추적하여 정답 수열을 구해내기
# LCS를 구하는 방법과 역추적하는 방법은 기억해둘 것!

import sys
input = sys.stdin.readline

X = input().rstrip()
Y = input().rstrip()
LCS = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]

for i in range(1, len(X) + 1):
    for j in range(1, len(Y) + 1):
        if X[i - 1] == Y[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else: # X[i] != Y[j]:
            LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])
print(LCS[-1][-1])

answer = ''
i, j = len(X), len(Y)
count = LCS[-1][-1]
while count > 0:
    if LCS[i - 1][j] == count:
        i -= 1
    elif LCS[i][j - 1] == count:
        j -= 1
    else:
        i, j = i - 1, j - 1
        answer = answer + X[i]
        count -= 1
print(answer[::-1])


