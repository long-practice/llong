class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        answer = -1

        n = len(gas)
        i = 0
        while i < n:
            rest_gas = 0
            j = 0
            while j < n:
                rest_gas += gas[(i + j) % n] - cost[(i + j) % n]
                if rest_gas < 0:
                    i += j + 1
                    break
                j += 1
            else:
                answer = i
                break

        return answer