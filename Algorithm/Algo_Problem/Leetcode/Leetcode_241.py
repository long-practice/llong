class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        answer = []

        elements = []
        num = ''
        for e in expression:
            if e in '+-*':
                elements.append(num)
                elements.append(e)
                num = ''
            else:
                num += e
        elements.append(num)
        oper_res = [[[] for _ in range(len(elements) + 1)] for _ in range(len(elements) + 1)]

        def func(left, right):
            if not oper_res[left][right]:
                if left + 1 == right:
                    oper_res[left][right].append(elements[left])
                else:
                    for i in range(left, right):
                        if i % 2:
                            left_res = func(left, i)
                            right_res = func(i + 1, right)

                            for l in left_res:
                                for r in right_res:
                                    oper_res[left][right].append(str(eval(l + elements[i] + r)))
            return oper_res[left][right]

        res = func(0, len(elements))
        answer = sorted([int(r) for r in res])

        return answer