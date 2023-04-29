class Solution:
    def numberOfWeeks(self, m: List[int]) -> int:
        return sum(m) if max(m) <= sum(m) - max(m) else (sum(m) - max(m)) * 2 + 1