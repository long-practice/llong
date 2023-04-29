class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        answer = 0
        while g and s:
            greed, cookie = g.pop(), s.pop()
            while g and greed > cookie:
                greed = g.pop()
            if greed <= cookie:
                answer += 1

        return answer