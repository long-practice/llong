# 2018 카카오 블라인드 채용
# 자동완성
# https://programmers.co.kr/learn/courses/30/lessons/17685

import sys
sys.setrecursionlimit(int(1e6))


class node():
    def __init__(self, c):
        self.c = c
        self.v = 0
        self.children = []

    def insert(self, word, i):
        self.v += 1
        next_node = None
        if i < len(word):
            for n in self.children:
                if n.c == word[i]:
                    next_node = n
                    break
            else:
                self.children.append(node(word[i]))
                next_node = self.children[-1]
            next_node.insert(word, i + 1)
        return

    def search_node(self, count):
        for n in self.children:
            if n.v == 1:
                count += 1
            else:
                count = n.search_node(count + n.v)
        return count


class trie():
    def __init__(self):
        self.root = node('root')

    def insert_word(self, word):
        return self.root.insert(word, 0)

    def search(self):
        return self.root.search_node(0)


def solution(words):
    t = trie()
    for word in words:
        t.insert_word(word)

    return t.search()
