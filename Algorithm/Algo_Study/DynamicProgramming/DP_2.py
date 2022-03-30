# 개미전사

# 해결방법
# 인접한 식량창고에는 식량을 약탈할 수 없음
# f(n) = f(n) + f(n - 2)의 점화식이 성립
# 그러나 f(n - 1)의 값이 더 클 수 있으므로 둘 사이의 최대값으로 f(n) 결정
# 첫 번째 식량창고부터 약탈할 때와 두 번째 식량창고부터 약탈할 때를 나누어 계산
# 그러나 첫 번째 식량창고를 약탈하는 것이 유리하다면 f(2) = f(1)이 되어야 함

# 예시
# 4개의 식량창고
# 1 3 1 5 에서는 두 번째와 네 번째의 식량 창고를 약탈할 경우 8의 식량을 얻을 수 있음(최대)

# 풀이
N = int(input())
foods = list(map(int, input().split(' ')))

# DP 리스트 생성
answer_array =[0 for _ in range(N)]
answer_array[0], answer_array[1] = foods[0], max(foods[0], foods[1])

# index = 2부터 DP 테이블 초기화
# f(n) = max(dp(n - 2) + f(n), dp(n - 1)
for i, food in enumerate(foods[2:], start = 2):
    answer_array[i] = max(foods[i] + answer_array[i - 2], answer_array[i - 1])

print(answer_array[-1])