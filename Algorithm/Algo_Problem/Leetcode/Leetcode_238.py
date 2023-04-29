class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0 for _ in range(len(nums))]

        V = 1
        for n in nums:
            if n:
                V *= n

        if nums.count(0) == 1:
            answer[nums.index(0)] = V
        elif nums.count(0) == 0:
            for i in range(len(nums)):
                answer[i] = V // nums[i]

        return answer
