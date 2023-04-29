class WordDictionary:
    def __init__(self):
        self.trie = {'': {}}

    def addWord(self, word: str) -> None:
        curr = self.trie['']
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['/'] = word

    def search(self, word: str) -> bool:
        def search_word(i, curr):
            if i < len(word):
                c = word[i]
                if c != '.':
                    if c not in curr.keys():
                        return False
                    return search_word(i + 1, curr[c])
                else:
                    for k in curr.keys():
                        if k != '/' and search_word(i + 1, curr[k]):
                            return True
                    return False
            else:
                return '/' in curr.keys()

        return search_word(0, self.trie[''])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)