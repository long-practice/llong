class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        b_pow, w = 0, 1
        while b:
            b_pow += w * b.pop()
            w *= 10

        answer = 1
        while b_pow:
            if b_pow & 1:
                answer = (answer * a) % mod
            b_pow >>= 1
            a = (a * a) % mod

        return answer