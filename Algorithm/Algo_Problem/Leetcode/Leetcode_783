# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []

        def traversal(node):
            if node:
                traversal(node.left)
                nums.append(node.val)
                traversal(node.right)

        traversal(root)
        return min(abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1))