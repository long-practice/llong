# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def connect(node, key):
            if node:
                if node.val < key:
                    node.right = connect(node.right, key)
                else:
                    node.left = connect(node.left, key)
            else:
                node = TreeNode(val=key)
            return node

        return connect(root, val)