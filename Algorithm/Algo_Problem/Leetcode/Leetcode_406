class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = deque([])
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            answer.insert(k, (h, k))
        return answer