class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        char_dict1, char_dict2 = Counter(word1), Counter(word2)
        return self.can_make_distinct_equal(char_dict1, char_dict2)


    def can_make_distinct_equal(self, d1, d2):
        d1_keys, d2_keys = tuple(d1.keys()), tuple(d2.keys())
        for key1 in d1_keys:
            for key2 in d2_keys:
                self.swap(d1, d2, key1, key2)
                if self.same_distinct_keys_length(d1, d2):
                    return True
                self.swap(d1, d2, key2, key1)
        return False


    def swap(self, d1, d2, k1, k2):
        d1[k1], d2[k1] = d1[k1] - 1, d2[k1] + 1
        d1[k2], d2[k2] = d1[k2] + 1, d2[k2] - 1


    def same_distinct_keys_length(self, d1, d2):
        l1 = [k for k in d1.keys() if d1[k]]
        l2 = [k for k in d2.keys() if d2[k]]
        return len(l1) == len(l2)

