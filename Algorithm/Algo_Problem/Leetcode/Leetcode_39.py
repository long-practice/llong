class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def get_combsum(L, res, S):
            if S > target:
                return
            elif S == target:
                answer.append(res)
            else:
                for i in range(L, len(candidates)):
                    get_combsum(i, res + [candidates[i]], S + candidates[i])

        get_combsum(0, [], 0)
        return answer