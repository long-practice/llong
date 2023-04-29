class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        table = [0 for _ in range(sum(stones) // 2 + 1)]
        for stone in stones:
            for i in range(len(table) - 1, stone - 1, -1):
                table[i] = max(table[i], table[i - stone] + stone)
        return min(sum(stones) - 2 * x for x in table)