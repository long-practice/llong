# 단어 수학

# 1. 입력 받은 문자열을 사전에 알파벳으로 키를 설정 값은 자릿수에 해당하는 값으로 초기화(DDD => D: 111)
# 2. 사전의 키와 값들을 하나의 튜플로 묶고 값을 기준 내림차순 정렬
# 3. 값이 큰 키에 대해 9부터 차례대로 값을 부여

# 과정 1.
import sys
input = sys.stdin.readline
N = int(input().rstrip('\n'))
words = []
num_char = dict()
answer = []
for _ in range(N):
    words.append(input().rstrip('\n'))
    for i in range(1, len(words[-1]) + 1):
        num_char[words[-1][-i]] = num_char.get(words[-1][-i], 0) + 10 ** (i - 1)

# 과정 2.
key_value = [(k, v) for k, v in num_char.items()]
key_value.sort(reverse = True, key = lambda x : x[1])

# 과정 3.
nums = [x for x in range(9, 9 - len(num_char.keys()), - 1)]
value = 0
for key_weight, num in zip(key_value, nums):
    value += num * key_weight[1]
print(value)