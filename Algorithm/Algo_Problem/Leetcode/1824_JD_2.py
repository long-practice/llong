class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        answer = 0
        loc, lane = 1, 2
        while loc < len(obstacles):
            if obstacles[loc] == lane:
                answer += 1
                loc -= 1
                cant = (1 << lane) | (1 << obstacles[loc])
                f = lambda x: int(bool(x))
                while loc + 1 < len(obstacles) and f(cant & 2) + f(cant & 4) + f(cant & 8) == 1:
                    cant |= (1 << obstacles[loc + 1])
                    loc += 1
                jump_bit = (15 - cant) >> 1
                lane = int(math.log2(jump_bit)) + 1
            loc += 1
        return answer