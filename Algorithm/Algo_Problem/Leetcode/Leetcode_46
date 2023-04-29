class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        idx = [False for _ in range(len(nums))]

        def func(res):
            if len(res) == len(nums):
                answer.append(res)
            else:
                for i in range(len(nums)):
                    if not idx[i]:
                        idx[i] = True
                        func(res + [nums[i]])
                        idx[i] = False

        func([])
        return answer