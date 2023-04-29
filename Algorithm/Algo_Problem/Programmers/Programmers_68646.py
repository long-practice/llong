def solution(a):
    answer = [a[0], a[-1]]
    m = a[0]
    min_idx = a.index(min(a))
    for i in range(1, min_idx + 1):
        if a[i] < m:
            answer.append(a[i])
            m = a[i]

    m = a[-1]
    for i in range(len(a) - 2, min_idx - 1, -1):
        if a[i] < m:
            answer.append(a[i])
            m = a[i]
    return len(list(set(answer)))