class Trie:
    def __init__(self):
        self.count = 0
        self.children = {}

    def insert(self, word):
        curr = self
        for c in word:
            curr.children[c] = curr.children.get(c, Trie())
            curr.count += 1
            curr = curr.children[c]

    def search(self, query):
        curr = self
        for q in query:
            if q == '?':
                return curr.count
            if q not in curr.children.keys():
                return 0
            else:
                curr = curr.children[q]
        return curr.count


def solution(words, queries):
    answer = []
    Tries = [Trie() for _ in range(10001)]
    revTries = [Trie() for _ in range(10001)]

    for word in words:
        Tries[len(word)].insert(word)
        revTries[len(word)].insert(word[::-1])

    for query in queries:
        if query[-1] == '?':
            answer.append(Tries[len(query)].search(query))
        else:
            answer.append(revTries[len(query)].search(query[::-1]))
    return answer