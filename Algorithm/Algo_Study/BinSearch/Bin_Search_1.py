# 부품 찾기

# 해결 방법
# 1. 이진 탐색을 이용한 리스트 내 해당 값 존재 여부 확인
# 2. 계수 정렬을 하여 해당 값의 인덱스가 0의 여부 확인
# 3. 집합 자료형을 이용하여 해당 값이 집합 내부에 있는지 여부 확인

# 예시
# 가게 부품: [8, 3, 7, 9, 2]
# 손님 요청: [5, 7, 9]
# 답: no yes yes

# 이진 탐색 재귀함수 이용
def bin_Search_recursion(request, start, end):
    if start > end:
        return False

    mid = (start + end) // 2
    if component[mid] > request:
        return bin_Search_recursion(request, start, mid - 1)
    elif component[mid] < request:
        return bin_Search_recursion(request, mid + 1, end)
    else: # component[mid] == request:
        return True

# 이진 탐색 반복문 이용
def bin_Search_iteration(request, start, end):
    while start <= end:
        mid = (start + end) // 2
        if component[mid] > request:
            end = mid - 1
        elif component[mid] < request:
            start = mid + 1
        else:
            return True
    return False

N = int(input())
component = list(map(int, input().split(' ')))

M = int(input())
request = list(map(int, input().split(' ')))

# 이진 탐색(재귀함수 이용)
'''
# 이진 탐색 시 리스트 정렬 필수
component.sort()
for r in request:
    if bin_Search_recursion(r, 0, N - 1):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''


# 이진 탐색(반복문 이용)
'''
# 이진 탐색 시 리스트 정렬 필수
component.sort()
for r in request:
    if bin_Search_iteration(r, 0, N - 1):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''

'''
# 계수 정렬 이용
count_array = [0 for _ in range(100000)]
for c in component:
    count_array[c - 1] += 1

for r in request:
    if count_array[r - 1] > 0:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''

# 집합 자료형 이용
component_set = set(component)

for r in request:
    if r in component_set:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')