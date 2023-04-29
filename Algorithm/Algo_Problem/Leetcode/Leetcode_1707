class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        answer = []
        for x, m in queries:
            start, stop = 0, bisect_right(nums, m)
            num = 0
            bit = 2 ** m.bit_length()
            while bit:
                cut = bisect_left(nums, num + bit, start, stop)
                if cut != stop:
                    if cut != start and x & bit:
                        stop = cut
                    else:
                        start = cut
                        num += bit
                bit //= 2
            answer.append(num ^ x if start < stop else -1)
        return answer