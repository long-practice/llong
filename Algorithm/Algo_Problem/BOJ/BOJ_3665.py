import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    graph = [[True for _ in range(n + 1)] for _ in range(n + 1)]
    degrees = [0 for _ in range(n + 1)]
    prev_rank = list(map(int, input().rstrip().split()))
    higher = []
    for i, r in enumerate(prev_rank):
        graph[r][r] = False
        degrees[r] = i
        for h in higher:
            graph[r][h] = False
        higher.append(r)

    for _ in range(int(input().rstrip())):
        a, b = map(int, input().rstrip().split())
        if graph[a][b]:
            graph[a][b], graph[b][a] = False, True
            degrees[a], degrees[b] = degrees[a] + 1, degrees[b] - 1
        else:
            graph[a][b], graph[b][a] = True, False
            degrees[a], degrees[b] = degrees[a] - 1, degrees[b] + 1

    lines = n * (n - 1) // 2
    q = [i for i in range(1, n + 1) if degrees[i] == 0]
    res = []
    while lines:
        if len(q) == 1:
            curr = q.pop()
            for g in range(1, n + 1):
                if graph[curr][g]:
                    lines, degrees[g] = lines - 1, degrees[g] - 1
                    if not degrees[g]:
                        q.append(g)
            res.append(curr)
        else:
            print('IMPOSSIBLE')
            break
    else:
        res.append(q.pop())
        print(' '.join(map(str, res)))