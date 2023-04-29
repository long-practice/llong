class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = [0 for _ in range(int(2e4) + 1)]
        for n in nums:
            count[n] += 1

        sorted_array = []
        for i in range(-10000, 10001):
            for _ in range(count[i]):
                sorted_array.append(i)

        return sorted_array[-k]