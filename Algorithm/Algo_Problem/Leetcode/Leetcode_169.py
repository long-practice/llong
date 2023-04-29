class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for c in count:
            if count[c] > len(nums) // 2:
                return c