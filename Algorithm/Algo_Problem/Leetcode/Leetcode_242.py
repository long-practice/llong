class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(list(s)), sorted(list(t))
        if len(s) == len(t):
            for i in range(min(len(s), len(t))):
                if s[i] != t[i]:
                    return False
        else:
            return False
        return True