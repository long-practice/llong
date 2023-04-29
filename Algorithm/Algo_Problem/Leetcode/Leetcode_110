# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(node):
            if node:
                if abs(get_depth(node.left) - get_depth(node.right)) > 1:
                    return False
                else:
                    return is_balanced(node.left) and is_balanced(node.right)
            return True

        def get_depth(node):
            return max(get_depth(node.left), get_depth(node.right)) + 1 if node else 0

        return is_balanced(root)