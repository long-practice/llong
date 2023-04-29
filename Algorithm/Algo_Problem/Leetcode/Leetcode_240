class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        answer = False

        def bisect(array):
            left, right = 0, len(array) - 1
            while left <= right:
                mid = (left + right) >> 1
                if array[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        idx = bisect(list(zip(*matrix))[0])
        for i in range(idx, -1, -1):
            j = bisect(matrix[i])
            if matrix[i][j] == target:
                answer = True
                break

        return answer

