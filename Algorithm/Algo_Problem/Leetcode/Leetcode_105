# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count_idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {v: i for i, v in enumerate(inorder)}

        def construct(left, right):
            root = None
            if left < right:
                i = inorder_idx[preorder[self.count_idx]]
                if left <= i < right:
                    self.count_idx += 1
                    root = TreeNode(inorder[i])
                    root.left = construct(left, i)
                    root.right = construct(i + 1, right)
            return root

        return construct(0, len(preorder))