# 큰 수의 법칙

# 해결방법
# 한 사이클을 배열 내 가장 큰 수를 연속으로 K번 더한 후 두번 째로 큰 수 더한다
# 이후 사이클을 반복하여 큰 수를 구한다

# 예시
# N, M, K = 5, 8, 3
# data = 2, 4, 5, 4, 6
# 배열 내 가장 큰 수는 6, 두 번째로 큰 수는 5
# 한 개의 숫자는 연속으로 3번 까지만 더할 수 있는 것을 고려하면
# 한 사이클은 다음과 같이 구성이 가능하다
# 1 cycle: 6 + 6 + 6 + 5
# 총 M번을 더할 수 있으므로
# (6 + 6 + 6 + 5) + (6 + 6 + 6 + 5) = 46
# 만약 M이 10이라면
# 2 * cycle + 2 * (가장 큰 수) = 46 + 2 * 6 = 58


# 풀이
# M: 주어진 수들을 몇 번 더하는 지 값을 저장
# K: K번을 초과하여 연속으로 더할 수 없음
# N: 배열의 크기 / data: 배열 내 데이터
N, M, K = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

# 배열을 오름차순으로 정렬
# 배열의 가장 마지막에 있는 원소가 가장 큰 수, 바로 앞에 있는 수가 두번 째로 큰 수
data.sort()
first_most_max = data[-1] # data[N - 1]
second_most_max = data[-2] # data[N - 2]

# 한 개의 사이클은 가장 큰 수를 K번을 연속으로 더하고 두번 째로 큰 수를 더한 값
cycle = K * first_most_max + second_most_max

# M 번을 더할 때 1사이클은 M을 K + 1을 나눈 몫 만큼 사이클이 등장
# 나머지 만큼 가장 큰 수를 더해주면 가장 큰 수를 만들 수 있음
answer = (M // (K + 1)) * cycle + (M % (K + 1)) * first_most_max
print(answer)


# cycle을 구하는 것 대신 가장 큰 수와 두번 째로 큰 수가 각각 몇 번 등장하는지 알 수 있음
# cycle 만큼 두번 째로 큰 수가 등장한다는 것을 생각하면 다음과 같은 코드작성 가능
answer = (M // (K + 1)) * second_most_max + (M - M // (K + 1)) * first_most_max
print(answer)