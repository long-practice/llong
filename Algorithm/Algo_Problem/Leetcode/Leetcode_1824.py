class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        answer = 0

        def can_go(lane, cant):
            bits = (15 - cant) >> 1
            l = 1
            while bits:
                if bits & 1:
                    yield l
                l += 1
                bits >>= 1

        prev = [0, 1, 0, 1]
        for loc in range(1, len(obstacles)):
            curr = [0]
            for lane in range(1, 4):
                if lane != obstacles[loc]:
                    count = prev[lane]
                    cant_jump = (1 << obstacles[loc]) | (1 << lane)
                    for l in can_go(lane, cant_jump):
                        count = min(count, prev[l] + 1)
                    curr.append(count)
                else:
                    curr.append(int(1e6))

            for i in range(3):
                prev[-1 - i] = curr.pop()

        answer = min(prev[1:])
        return answer
