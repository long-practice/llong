class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bisect(left, right, trg):
            while left <= right:
                mid = (left + right) >> 1
                if numbers[mid] < trg:
                    left = mid + 1
                elif numbers[mid] > trg:
                    right = mid - 1
                else:
                    return mid
            return False

        answer = []
        for i in range(len(numbers) - 1):
            another_i = bisect(i + 1, len(numbers) - 1, target - numbers[i])
            if another_i:
                answer.extend([i + 1, another_i + 1])
                break

        return answer