def possible(a, b, g, s, w, t, mid):
    Gold, Silver, Total = 0, 0, 0

    for i in range(len(w)):
        d = mid // t[i]
        n = d // 2 + d % 2

        Total += min(g[i] + s[i], n * w[i])
        Gold += min(g[i], n * w[i])
        Silver += min(s[i], n * w[i])

    return a <= Gold and b <= Silver and a + b <= Total


def solution(a, b, g, s, w, t):
    m, M = 0, int(1e15)
    while m <= M:
        mid = (m + M) >> 1

        if possible(a, b, g, s, w, t, mid):
            M = mid - 1
        else:
            m = mid + 1

    return m