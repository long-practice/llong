class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        answer = 0

        for i in range(len(str(num)) - k + 1):
            divisor = int(str(num)[i: i + k])
            if divisor and not num % divisor:
                answer += 1

        return answer