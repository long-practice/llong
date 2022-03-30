# 바닥 공사

# 해결방안
# f(n) = f(n - 1) + f(n - 2) * 2의 점화식이 성립
# f(n - 2)에서 1 X 2 타일을 위아래로 두 개 혹은 1 X 1 타일을 한 개 배치하는 방법
# f(n - 1)에서 2 X 1 타일을 한 개 배치하는 방법
# 따라서 위의 점화식이 성립

# 풀이
N = int(input())
answer_array = [0 for _ in range(N)]

answer_array[0] = 1
answer_array[1] = 3

# f(n) = f(n - 1) + f(n - 2) * 2 구현
for i in range(2, N):
    answer_array[i] = answer_array[i - 1] + (answer_array[i - 2] * 2)

print(answer_array[-1])