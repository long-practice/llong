class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer, M = nums[0], nums[0]
        for i in range(1, len(nums)):
            M = (max(nums[i] + M, nums[i]))
            answer = max(answer, M)
        return answer