# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        node_trace = {}

        def get_trace(node, tr):
            nonlocal max_depth
            if node:
                tr.append(node)
                max_depth = max(len(tr), max_depth)
                node_trace[node] = tr[:]
                get_trace(node.left, tr)
                get_trace(node.right, tr)
                tr.pop()

        get_trace(root, [])

        deepest_node = [x for x, tr in node_trace.items() if len(tr) == max_depth]
        count_node = {}
        M = 0
        for d_n in deepest_node:
            for n in node_trace[d_n]:
                count_node[n] = count_node.get(n, 0) + 1
                M = max(M, count_node[n])

        total_trace = [(len(node_trace[x]), x) for x in list(count_node.keys()) if count_node[x] == M]
        total_trace.sort()

        return total_trace[-1][1]