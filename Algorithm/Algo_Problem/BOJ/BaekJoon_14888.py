# 연산자 끼워넣기

# 풀이 방법
# 각 연산자 별로 배치할 수 있는 방법에 따라 배치하고
# 이후 각 수들을 연산하여 답을 구해냄

from itertools import permutations

N = int(input())
numbers = list(map(int, input().split(' ')))
operator_count = list(map(int, input().split(' ')))

def calculate(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == '*':
        return num_1 * num_2
    else: # operator == '/':
        if (num_1 < 0 and num_2 > 0) or (num_1 > 0 and num_2 < 0):
            return -1 * (abs(num_1) // abs(num_2))
        else:
            return num_1 // num_2

answer = set()
operators = []
for o, count in zip("+-*/", operator_count):
    operators.extend([o] * count)

for operator in set(permutations(operators)):
    result = numbers[0]
    for i, o in enumerate(operator, start = 1):
        result = calculate(result, numbers[i], o)
    answer.add(result)
print(max(answer))
print(min(answer))