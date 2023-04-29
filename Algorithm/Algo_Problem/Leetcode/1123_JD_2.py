# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lr_depth = {}

        def get_depth(node):
            depth = 0
            if node:
                l, r = get_depth(node.left), get_depth(node.right)
                lr_depth[node] = (l, r)
                depth = max(l, r) + 1
            return depth

        get_depth(root)

        def get_lca(node):
            if node:
                if lr_depth[node][0] == lr_depth[node][1]:
                    return node
                elif lr_depth[node][0] > lr_depth[node][1]:
                    return get_lca(node.left)
                else:
                    return get_lca(node.right)

        return get_lca(root)