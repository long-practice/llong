# 3번
# 오늘은 A대학의 학생 N명과 B대학의 학생 M명이 만나는 날이다.
# 이들이 만나는 장소에는 크고 길이가 긴 식탁이 하나 있어서, 한쪽에는 A대학 학생이, 다른 한쪽에는 B대학 학생이 앉을 예정이다.
#
# A대학 학생은 1부터 N까지, B대학 학생들은 1부터 M까지 번호가 붙어 있다. 의자에 앉을 때는 번호가 증가하는 순서대로 앉는다.
# 모든 일정이 끝나면 학생들은 서로 악수를 한다. 한 사람은 최대 한 사람과 악수를 할 수 있다.
# 이 때, 팔이 교차하면 악수를 할 때 불편하기 때문에, 팔이 교차하지 않게 악수를 해야 한다. 악수를 하지 못하는 사람이 생길 수도 있다.

# 즉, 총 K쌍이 생긴 상황에서, 어떤 i (1 <= i <= K)에 대해,
# i번째 쌍이 A대학의 x_i번째, B대학의 y_i번째 학생이 악수를 했다고 하면 x_i < x_j이면 y_i < y_j여야 한다.

# 학생의 성격을 1 이상, C 이하의 정수로 나타낼 수 있다.
# 성격이 a인 사람과 b인 사람이 악수를 할 경우, W[a][b]만큼의 만족도를 얻는다고 한다.
# 모든 학생들의 성격을 알고 있을 때, 가능한 만족도의 합의 최댓값을 구하고 싶다. 이를 구하는 프로그램을 작성하라.

# 2명의 A대학교 학생
# 3명의 B대학교 학생
# 2가지 성격 유형

# 1번 성격과 1번 성격이 악수: 1의 만족도
# 1번 성격과 2번 성격이 악수(2번 성격과 1번 성격이 악수): 10의 만족도
# 2번 성격과 2번 성격이 악수: 10의 만족도

# A 대학교 학생들의 성격: 1, 2
# B 대학교 학생들의 성격: 1, 2, 2

# 2 3 2
# 1 10
# 10 10
# 1 2
# 1 2 2
# answer: 20

import sys
input = sys.stdin.readline

N, M, C = map(int, input().rstrip().split())
W = [list(map(int, input().rstrip().split())) for _ in range(C)]
a_ls = list(map(int, input().rstrip().split()))
b_ls = list(map(int, input().rstrip().split()))
table = [[0 for _ in range(M+1)] for _ in range(N+1)]


def func(a, b):
    if a == N or b == M:
        return 0
    if not table[a][b]:
        table[a][b] = W[a_ls[a] - 1][b_ls[b] - 1] + func(a + 1, b + 1)
        table[a][b] = max(table[a][b], func(a + 1, b), func(a, b + 1))
    return table[a][b]


print(func(0, 0))