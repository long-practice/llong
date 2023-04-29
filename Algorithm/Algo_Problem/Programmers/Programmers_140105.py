def solution(n, count):
    mod = int(1e9) + 7
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    table[1][1] = 1

    for count_idx in range(n + 1):
        for n_idx in range(2, n + 1):
            table[n_idx][count_idx] = table[n_idx - 1][count_idx - 1] + 2 * (n_idx - 1) * table[n_idx - 1][count_idx]

    return table[n][count] % mod