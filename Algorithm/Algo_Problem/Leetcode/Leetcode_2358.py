class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return int((-1 + (1 + 8*len(grades))**0.5) / 2)