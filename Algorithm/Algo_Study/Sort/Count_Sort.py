# 계수정렬
# 시간복잡도 O(N + K)
# 리스트 내 원소의 범위가 작을 경우에 굉장히 유용하게 사용될 수 있음

# K개의 값을 갖는 리스트를 만들고 정렬해야 하는 값들로 인덱스를 매칭시켜 원소들의 개수를 카운팅
# 이후 카운팅된 개수만큼 해당 값을 출력

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 4, 8]

# array의 최대값: 9, 최소값: 0
# 각각의 값이 카운팅 리스트의 인덱스에 매칭될 수 있도록 리스트 생성
count_list = [0 for x in range(10)]
sorted_array = []

# 리스트 내 각각의 원소가 몇개가 있는지 카운팅
for a in array:
    count_list[a] += 1

# 카운팅된 원소의 개수만큼 반복해서 인덱스를 출력
for i, count in enumerate(count_list):
    for c in range(count):
        sorted_array.append(i)

print(sorted_array)