class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palin(s):
            return s == s[::-1]

        def get_answer(s):
            for size in range(len(s), 0, -1):
                for i in range(len(s) - size + 1):
                    if is_palin(s[i:i + size]):
                        return s[i:i + size]

        answer = get_answer(s)
        return answer