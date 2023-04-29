class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {chr(k): 0 for k in range(ord('A'), ord('Z') + 1)}

        h, contain_char = [], set()
        left, right = 0, 0
        while right < len(s):
            char_dict[s[right]] += 1
            if char_dict[s[right]] == 1:
                contain_char.add(s[right])
            right += 1

            while True:
                rest = right - left - max([char_dict[x] for x in contain_char])
                if rest > k:
                    char_dict[s[left]] -= 1
                    if char_dict[s[left]] == 0:
                        contain_char.remove(s[left])
                    left += 1
                else:
                    break

            heapq.heappush(h, left - right)

        answer = -heapq.heappop(h)
        return answer
