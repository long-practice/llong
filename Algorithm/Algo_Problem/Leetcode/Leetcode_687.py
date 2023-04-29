# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def search_path(parent, node):
            if node:
                left, longest_left = search_path(node, node.left)
                right, longest_right = search_path(node, node.right)
                if parent and parent.val == node.val:
                    return max(left, right) + 1, max(left + right, longest_left, longest_right)
                else:
                    return 0, max(left + right, longest_left, longest_right)
            return 0, 0
        return search_path(None, root)[1]