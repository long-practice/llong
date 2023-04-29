class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        negative, positive, zero = [], [], []
        for n in nums:
            if n > 0:
                positive.append(n)
            elif n < 0:
                negative.append(n)
            else:
                zero.append(n)

        def get_triplets(L, S):
            res = set()
            for i in range(len(L) - 1):
                for j in range(i + 1, len(L)):
                    if -(L[i] + L[j]) in S:
                        r = sorted([L[i], L[j], -(L[i] + L[j])])
                        res.add(tuple(r))
            return res

        def get_triplets_with_zero(L, S):
            res = set()
            for l in L:
                if -l in S:
                    if l > 0:
                        l *= -1
                    res.add((l, 0, -l))
            return res

        nset, pset = set(negative), set(positive)
        answer |= get_triplets(negative, pset) | get_triplets(positive, nset)
        if zero:
            answer |= get_triplets_with_zero(negative, pset) | get_triplets(positive, nset)
        if len(zero) >= 3:
            answer |= set([(0, 0, 0)])

        return answer
