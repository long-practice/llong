def solution(info, edges):
    tree = [0 for _ in range(len(info))]
    memo = [0 for _ in range(1 << len(info))]
    for edge in edges:
        a, b = edge
        tree[a] |= 1 << b

    def dfs(curr, can_go, s, w):
        if s - w > 0 and not memo[curr]:
            memo[curr] = s
            node = 1
            while node < len(info):
                if can_go & (1 << node):
                    dfs(curr | (1 << node), (can_go | tree[node]) ^ (1 << node), s + (info[node] ^ 1), w + info[node])
                node += 1

    dfs(1 << 0, tree[0], 1, 0)
    return max(memo)