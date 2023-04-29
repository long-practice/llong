class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letter = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        def func(d, result, res):
            if d < len(digits):
                for i in num_letter[int(digits[d])]:
                    if d == len(digits) - 1:
                        result.append(res + i)
                    else:
                        result = func(d + 1, result, res + i)
            return result

        return func(0, [], '')
