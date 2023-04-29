class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        nums = [x + 1 for x in range(n)]

        def comb(L, res):
            if len(res) == k:
                answer.append(res)
            else:
                for i in range(L, n):
                    comb(i + 1, res + [nums[i]])

        comb(0, [])

        return answer