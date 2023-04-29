# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0

        def get_answer(node):
            nonlocal answer
            if node:
                answer += node.val if low <= node.val <= high else 0
                get_answer(node.left)
                get_answer(node.right)

        get_answer(root)
        return answer