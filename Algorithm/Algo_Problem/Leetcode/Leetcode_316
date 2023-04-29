class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        rest = Counter(s)
        in_stack = 0

        for c in s:
            if not 1 << (ord(c) - ord('a')) & in_stack:
                while stack and stack[-1] >= c and rest[stack[-1]]:
                    in_stack ^= 1 << (ord(stack.pop()) - ord('a'))
                stack.append(c)
                in_stack ^= 1 << (ord(c) - ord('a'))
            rest[c] -= 1

        return ''.join(stack)
