# # 사다리 조작
# #
# # # step 1. 문제상황 구현, 사다리의 위치를 2차원 리스트(ladder)로 구현
# #           r행 c열에 배치되면 리스트에(r - 1, c - 1)을 추가
# #
# # # step 2. 백트래킹 시작
# #           추가할 수 있는 가로선은 0개에서 부터 3개 까지이므로 recursion_depth를 3으로 하여
# #           해당 자리를 포함해서 1개, 2개, 3개 배치할 경우를 판단
# #           만약 게임종료 조건을 만족했다면 다음 탐색 부터는 해당 개수보다 작은 개수(count)만을 놓아서 탐색
# #
# # # step 3. 사다리 설치(set_ladder)
# #           사다리를 설치할 수 있으면 사다리를 설치. 백트래킹 도중 연속해서 사다리를 놓는 일이 없도록
# #           인덱스를 잘 조정하여 사다리 설치
# #
# # # step 4. 사다리를 최대 개수로 설치를 했다면 사다리 게임 시작(play_the_game)
# #           i번째 열의 결과가 i라면 백트래킹 종료(return True)
# #
# # # step 5. 백트래킹 결과 값(사다리 개수) 반환
#
#
# # # step 1
# # # 문제 상황 구현
# import sys
# def input():
#     return sys.stdin.readline().rstrip('\n')
# sys.setrecursionlimit(int(1e4))
#
# N, M, H = map(int, input().split(' '))
#
# # 사다리가 어디에 설치되어 있는지 ladder에 기록
# # 사다리는 세로줄 N개라면 N - 1개의 구간에 설치가 될 수 있지만
# # 나중에 게임을 하는 과정에서 사다리가 있는지 유무를 판단할 때 인덱스 에러를 효과적으로 피하기 위해
# # 가장 우측은 False로 도핑
# ladder = [[False for _ in range(N)] for _ in range(H)]
# for _ in range(M):
#     r, c = map(int, input().split(' '))
#     ladder[r - 1][c - 1] = True
#
# # step 3
# # 사다리 설치
# count = 4
# def set_ladder(L, curr):
#     # 사다리게임 시작
#     # 만약 count 이상으로 사다리를 놓으면 함수 종료(이 경우 게임 종료 조건을 1번이라도 만족한 후에 적용)
#     global count
#     if count <= L:
#         return
#
#     # 만약 게임 종료 조건을 만족했다면 count를 현재 사다리를 놓은 개수로 수정
#     if play_the_game():
#         count = L
#         return
#
#     # 만약 사다리를 3개 설치했다면(이 경우에는 게임 종료 조건을 1번도 만족하지 못한 경우 적용)
#     if L == 3:
#         return
#
#     # 설치할 최대 개수(count)만큼 설치를 하지 않았다면
#     if L < count:
#         row, col = curr
#         # 설치하려는 위치(r, c)에 사다리가 없고
#         # 양 옆에 사다리가 없으면 사다리를 설치, 그러나 이전 함수에서 열의 값이 + 2 인채로 col에 저장되었으니 오른쪽만 확인하면 됨
#         # 설치하게 되면 ladder_loc에 설치한 위치를 추가
#         for r in range(row, H):
#             col = col if r == row else 0 # 2차원 리스트 행, 열 값을 이용하여 백트래킹할 시 유용함. 기억할 것!!
#             for c in range(col, N - 1):
#                 # 만약 현재 위치에 사다리가 놓여져 있으면
#                 # 그 다음 위치에도 사다리를 놓을 수 없으므로 c += 1
#                 if ladder[r][c]:
#                     c += 1
#                 else: # not ladder[r][c]:
#                     ladder[r][c] = True
#                     # 설치한 곳 바로 옆에는 설치가 불가하므로 c + 2
#                     set_ladder(L + 1, (r, c + 2))
#                     ladder[r][c] = False
#     return
#
# # step 4
# # 사다리 게임 시작
# # 맨 위에 있는 숫자 한개씩 진행
# # 만약 해당 위치에서 좌우측에 사다리가 있는지 확인(가장자리 예외처리)
# # 사다리가 존재하면 열 변경
# # 마지막 행에서 i가 i번 째 열에 도착했는지 확인
# def play_the_game():
#     for c in range(0, N):
#         k = c
#         # 위에서부터 한 줄씩 내려오기
#         for r in range(0, H):
#             # 사다리 판별
#             # 사다리가 없으면 이전 행에 있는 값들을 그대로 저장하면 됨 사다리가 있으면 열의 값 변경
#             # ladder[r][N - 1]은 False로 도핑했기 때문에 인덱스 에러가 나지 않음
#             if ladder[r][k]:
#                 k += 1
#             elif ladder[r][k - 1] and k > 0:
#                 k -= 1
#         # i 번째 열이 i열에 도착하지 않으면False 반환
#         if k != c:
#             return False
#     # i 번째 열의 게임 결과가 i면 True 반환
#     return True
#
# # step 2
# # 백트래킹 시작
# set_ladder(0, (0, 0))
#
# if 0 <= count <= 3:
#     print(count)
# else:
#     print(-1)


def check(pos):
    for i in range(len(pos[0]) + 1):
        pre = i
        for j in range(len(pos)):
            if i < len(pos[0]) and pos[j][i]:
                i += 1
            elif i > 0 and pos[j][i - 1]:
                i -= 1
        if pre != i:
            return False
    return True


def dfs(pos, n, m, line):
    if m <= n:
        return m
    if n == 4:
        return 4
    if check(pos):
        return n
    odd = 0
    for i in line:
        if i % 2 == 1:
            odd += 1
    if odd > 3 - n:
        return 4
    for i in range(len(pos)):
        for j in range(len(pos[0])):
            if pos[i][j]:
                continue
            if j + 1 < len(pos[i]) and pos[i][j + 1]:
                continue
            if j - 1 > 0 and pos[i][j - 1]:
                continue
            pos[i][j] = True
            line[j] += 1
            m = min(m, dfs(pos, n + 1, m, line))
            pos[i][j] = False
            line[j] -= 1
    return m


n, m, p = map(int, input().split())
pos = [[False for j in range(n - 1)] for i in range(p)]
line = [0 for i in range(n - 1)]

for i in range(m):
    a = list(map(int, input().split()))
    b = a[1] - 1
    a = a[0] - 1
    pos[a][b] = True
    line[b] += 1

answer = dfs(pos, 0, 4, line)
if answer == 4:
    answer = -1

print(answer)