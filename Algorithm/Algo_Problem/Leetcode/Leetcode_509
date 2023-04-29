import numpy as np

class Solution:
    def fib(self, n: int) -> int:
        M = np.array([[1, 1], [1, 0]])
        mat = np.eye(2, dtype=int)

        while n:
            if n & 1:
                mat = M @ mat
            M = M @ M
            n >>= 1

        answer = mat @ np.array([[1], [0]])
        return answer[1, 0]