import numpy as np

class Solution:
    def climbStairs(self, n: int) -> int:
        return (np.linalg.matrix_power(np.array([[1, 1], [1, 0]]), n) @ np.array([[1], [0]]))[0, 0]