# 이진탐색

# 반으로 쪼개면서 탐색하기(mid 기준)
# 타깃 값보다 리스트의 가운데에 있는 수가 크면 리스트의 좌측 탐색(array[mid] > target)
# 타깃 값보다 리스트의 가운데에 있는 수가 작으면 리스트의 우측 탐색(array[mid] < target)
# 타깃 값과 리스트의 가운데에 있는 수가 같으면 해당 인덱스값 반환(array[mid] == target)
# 데이터의 수가 굉장히 많을 때 유용하게 사용할 수 있음
# 그러나 리스트가 정렬된 상태에서만 사용이 가능

# 재귀함수 이용
def Binary_Search_recursion(array, target, start, end):
    if start > end:
        return

    # 리스트의 가운데에 있는 원소의 인덱스(mid)
    mid = (start + end) // 2

    if array[mid] > target:
        return Binary_Search_recursion(array, target, start, mid - 1)
    elif array[mid] < target:
        return Binary_Search_recursion(array, target, mid + 1, end)
    else:
        return mid

# 반복문 이용
def Binary_Search_iteration(array, target):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return

input_number = list(input().split(' '))
input_number.sort(key=lambda x: int(x))
target_number = input()

start, end = 0, len(input_number) - 1

#answer = Binary_Search_recursion(input_number, target_number, start, end)
answer = Binary_Search_iteration(input_number, target_number)
print(answer if answer != None else "값이 존재하지 않습니다.")