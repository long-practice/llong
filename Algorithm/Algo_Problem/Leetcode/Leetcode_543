# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = self.get_depth(root.left) + self.get_depth(root.right) if root else 0
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), diameter) if root else 0

    def get_depth(self, node: Optional[TreeNode]) -> int:
        return max(self.get_depth(node.left), self.get_depth(node.right)) + 1 if node else 0