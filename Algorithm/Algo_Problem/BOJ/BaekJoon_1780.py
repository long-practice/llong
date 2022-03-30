# 색종이 붙이기 2

# 백트래킹을 이용하여 색종이 붙이기
# 1을 만났을때 순서대로 1X1, 2X2, 3X3 ... 순서대로 붙이되
# 만약 2X2를 못붙인다면 그 이상의 크기의 색종이도 붙일 수 없음
import sys
input = sys.stdin.readline

paper = [list(map(int, input().rstrip().split())) for _ in range(10)]
paper_type = [0, 5, 5, 5, 5, 5]
one_field = 0
for r in range(10):
    for c in range(10):
        if paper[r][c]:
            one_field += 1
answer = 100


def attaching(row, col, size, n):
    for r in range(row, row + size):
        for c in range(col, col + size):
            paper[r][c] = n


def can_attach(row, col, size):
    if row > 10 - size or col > 10 - size:
        return False
    else:
        for r in range(row, row + size):
            for c in range(col, col + size):
                if not paper[r][c]:
                    return False
    return True


def backtracking(row, col, count):
    global answer, one_field
    for r in range(row, 10):
        if r != row:
            col = 0
        for c in range(col, 10):
            if paper[r][c]:
                for m in range(1, 6):
                    if paper_type[m] <= 0:
                        continue

                    if can_attach(r, c, m):
                        if one_field - m * m == 0:
                            answer = min(answer, count + 1)
                            return

                        one_field -= m * m
                        attaching(r, c, m, 0)
                        paper_type[m] -= 1

                        backtracking(r, c + m, count + 1)

                        one_field += m * m
                        paper_type[m] += 1
                        attaching(r, c, m, 1)
                    else:
                        return
                return

if one_field:
    backtracking(0, 0, 0)
else:
    answer = 0
print(-1 if answer == 100 else answer)