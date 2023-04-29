import numpy as np


class Solution:
    def countVowelStrings(self, n: int) -> int:
        table = np.zeros((5, n), dtype=int)

        table[:, 0] = 1
        for r in range(5):
            for c in range(1, n):
                table[r, c] = np.sum(table[:r + 1, c - 1])

        return np.sum(table[:, -1])