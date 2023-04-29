# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = root.val if root else 0
        def get_path(node):
            nonlocal answer
            if node:
                left, right = get_path(node.left), get_path(node.right)
                max_l, max_r = max(0, left), max(0, right)
                answer = max(answer, max_l + max_r + node.val)
                return max(max_l, max_r) + + node.val
            return 0
        get_path(root)
        return answer