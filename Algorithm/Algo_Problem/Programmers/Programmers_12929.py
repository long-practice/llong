def solution(n):
    table = [1] + [0 for _ in range(15)]
    for i in range(1, n + 1):
        for j in range(i):
            table[i] += table[j] * table[(i - 1) - j]
    return table[n]