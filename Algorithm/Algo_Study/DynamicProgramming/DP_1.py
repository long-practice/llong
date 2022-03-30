# 1로 만들기

# 해결방법
# 연산을 할 때마다 가능한 수를 집합에 저장
# 해당 집합에서 수를 하나씩 가져와서 각 연산 진행
# 해당 집합에 1이 있으면 종료

# 예시
# 입력: 26 / 출력: 3
# 1회 연산 시: 25
# 2회 연산 시: 5
# 3회 연산 시: 1 (종료)

# 풀이
x = int(input())
x_set, temp = set([x]), set()
answer = 0

while 1 not in x_set:
    for num in x_set:
        if num % 5 == 0:
            temp.add(num // 5)
        if num % 3 == 0:
            temp.add(num // 3)
        if num % 2 == 0:
            temp.add(num // 2)
        temp.add(num - 1)
    answer += 1
    x_set = temp.copy()
    temp = set()
    print(x_set)

print(answer)