# 괄호 추가하기 1

# 괄호를 묶을 수 있는 경우의 수를 모두 파악, 연산자의 위치를 기준으로 좌, 우 숫자를 포함해서 묶으면 됨
# 한 번 괄호를 묶었으면 양 옆으로 이웃해 있는 연산자는 괄호로 묶을 수 없음
# 이 후 괄호를 묶으면서 각각의 수식을 계산
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums, operator = [], []
for i, c in enumerate(input().rstrip()):
    if i % 2:
        operator.append(c)
    else:
        nums.append(c)

combination = []

def get_combi(L, res):
    combination.append(res)
    for i in range(L, N // 2):
        get_combi(i + 2, res + [i])


def get_val(comb_arr):
    stack = [nums[0]]
    i = 0
    while i < N // 2:
        if i + 1 in comb_arr:
            stack.append(str(eval(stack.pop() + operator[i] + '(' + nums[i + 1] + operator[i + 1] + nums[i + 2] + ')')))
            i += 1
        else:
            stack.append(str(eval(stack.pop() + operator[i] + nums[i + 1])))
        i += 1
    return int(stack[0])

get_combi(1, [])
answer = []
for combi in combination:
    answer.append(get_val(combi))
print(max(answer))