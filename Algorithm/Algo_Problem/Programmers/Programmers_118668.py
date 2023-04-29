def solution(alp, cop, problems):
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    max_alp, max_cop = max(list(zip(*problems))[0]), max(list(zip(*problems))[1])
    table = [[int(1e5) for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    table[alp][cop] = 0

    for alp_idx in range(alp, max_alp + 1):
        for cop_idx in range(cop, max_cop + 1):
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if alp_idx >= alp_req and cop_idx >= cop_req:
                    next_alp_idx = min(alp_idx + alp_rwd, max_alp)
                    next_cop_idx = min(cop_idx + cop_rwd, max_cop)
                    table[next_alp_idx][next_cop_idx] = min(table[next_alp_idx][next_cop_idx],
                                                            table[alp_idx][cop_idx] + cost)

    answer = table[max_alp][max_cop]
    return answer
