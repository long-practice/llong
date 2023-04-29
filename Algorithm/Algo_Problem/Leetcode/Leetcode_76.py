class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M = len(set(t))

        compare = {}
        for c in t:
            compare[c] = compare.get(c, 0) + 1

        left, right = 0, 0
        interval, window_dict = [], {}
        while right < len(s) and left < len(s):
            window_dict[s[right]] = window_dict.get(s[right], 0) + 1
            if window_dict[s[right]] == compare.get(s[right], 0):
                M -= 1
            right += 1

            while not M:
                heapq.heappush(interval, (right - left, left, right))
                window_dict[s[left]] -= 1
                if window_dict[s[left]] < compare.get(s[left], 0):
                    M += 1
                left += 1

        answer = ""
        if interval:
            l, r = interval[0][1], interval[0][2]
            answer = s[l:r]

        return answer