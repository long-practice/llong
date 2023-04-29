class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]
        left_prod, right_prod = 1, 1
        for i in range(len(nums)):
            answer[i] *= left_prod
            answer[-i - 1] *= right_prod
            left_prod, right_prod = left_prod * nums[i], right_prod * nums[-i - 1]
        return answer
