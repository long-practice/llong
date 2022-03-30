# 버블정렬
# O(n**2)의 시간복잡도
# 매회전 시 가장 큰 원소부터 리스트 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 예시
# 1회전 시
# array = [5, 7, 0, 3, 1, 6, 2, 4, 8, 9]
# 2회전 시
# array = [5, 0, 3, 1, 6, 2, 4, 7, 8, 9]
# 3회전 시
# array = [5, 0, 3, 1, 6, 2, 4, 7, 8, 9]

for i in range(0, len(array) - 1):
    for j in range(1, len(array) - i):
        if array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
print(array)