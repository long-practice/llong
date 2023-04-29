class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.keys():
                curr[c] = {}
            curr = curr[c]
        curr['/'] = word

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.keys():
                curr = curr[c]
            else:
                break
        else:
            return '/' in curr.keys() and curr['/'] == word
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.keys():
                curr = curr[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)