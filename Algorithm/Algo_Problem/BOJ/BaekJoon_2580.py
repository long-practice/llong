# 스도쿠

# 백트래킹 이용
# 스도쿠의 유효성을 검사하기 위해
# row, col, subquad라는 2차원 리스트를 만들고
# 빈칸에 값을 채워넣을 경우 해당 리스트에 값을 True로 변경하여
# 중복되게 값을 할당하는 일이 없도록 조건 판별
# 또한 값을 채울 수 없는 경우 백트래킹을 통하여 맞는 수를 탐색

import sys
def input():
    return sys.stdin.readline().rstrip()

# 입력
array = [list(map(int, input().split(' '))) for _ in range(9)]

# row: 0행 ~ 8행까지 가로줄 유효성 판단하기 위한 리스트
# col: 0열 ~ 8열까지 세로줄 유효성 판단하기 위한 리스트
# subquad: 3X3 단위로 나뉘어진 구역의 유효성을 판단하기 위한 리스트
row = [[False for _ in range(9)] for _ in range(9)]
col = [[False for _ in range(9)] for _ in range(9)]
subquad = [[False for _ in range(9)] for _ in range(9)]

# 넣어야할 숫자들을 숫자별로 몇개인지 확인
# 빈칸이 아닌 칸들에 대해서 row, col, subquad 최신화

# 만약 1행 1열에 8이 있다면
# row 1에는 8이 있다는 것을 알리기위해 row[1][8 - 1] = True
# col, subquad도 마찬가지
# subquad는 계산방식이 조금 다름
# 위의 예를 살펴보면 1행 1열의 원소는 0번째 subquad이므로
# subquad[0][8 - 1] = True로 처리해야함
# 하나의 예를 더들면 5행 5열의 원소는 4번째 subquad이므로
# subquad[4][i - 1] = True로 처리
# 모든 r, c에 대해서 (r // 3 * 3 + c // 3)번째 subquad로 매칭이됨

# 만약 numbers가 [2, 3, 4, 1, 0, 0, 0, 0, 2]라면
# 1: 2개, 2: 3개, 3: 4개, 4: 1개, 9: 2개를 채워넣어야 함

# 0인 구간도 zero_fields 리스트에 저장
numbers = [9 for _ in range(9)]
zero_fields = []
for r in range(9):
    for c in range(9):
        i = array[r][c]
        if i:
            row[r][i - 1], col[c][i - 1], subquad[r // 3 * 3 + c // 3][i - 1] = True, True, True
            numbers[i - 1] -= 1
        else:
            zero_fields.append((r, c))

# 백트래킹 시작
# 만약 유효한 스도쿠가 발생되었을 시 즉시 백트래킹이 종료될 수 있도록 is_valid로 판별
# zero_fields만 값을 채워주면 되므로
# len(zero fields)만큼 recursion depth를 설정
is_valid = False
def backtrack(L):
    global is_valid
    if is_valid:
        return True
    if L == len(zero_fields):
        is_valid = True
        for a in array:
            for e in a:
                print(e, end=' ')
            print()
        return True
    else:
        r, c = zero_fields[L]
        can_num = set()
        # 빈칸에 넣을 수 있는 수를 탐색
        for i in range(1, 10):
            # 해당 숫자를 스도쿠에 넣을 수 있으면 탐색
            # 예를 들어 i가 만약 6인데 이미 9개의 6이 스도쿠에 배치가 되었다면 굳이 탐색할 필요가 없음
            if numbers[i - 1]:
                # 행에도 i라는 숫자가 없고, 열에도 i라는 숫자가 없고, subquad에도 i라는 숫자가 없으면 진행
                # not(A) & not(B) & not(C) == not(A || B || C)
                if row[r][i - 1] or col[c][i - 1] or subquad[r // 3 * 3 + c // 3][i - 1]:
                    continue
                else:
                    can_num.add(i)

        for i in can_num:
            row[r][i - 1], col[c][i - 1], subquad[r // 3 * 3 + c // 3][i - 1] = True, True, True
            array[r][c] = i
            numbers[i - 1] -= 1

            if backtrack(L + 1):
                return True

            row[r][i - 1], col[c][i - 1], subquad[r // 3 * 3 + c // 3][i - 1] = False, False, False
            array[r][c] = 0
            numbers[i - 1] += 1
    return False

backtrack(0)