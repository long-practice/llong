class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def get_subsets(L, res):
            answer.append(res)
            for i in range(L, len(nums)):
                get_subsets(i + 1, res + [nums[i]])

        get_subsets(0, [])
        return answer