class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []

        anagram_dict = {}
        for s in strs:
            k = ''.join(sorted(s))
            anagram_dict[k] = anagram_dict.get(k, []) + [s]

        for vlist in anagram_dict.values():
            answer.append(vlist)

        return answer
