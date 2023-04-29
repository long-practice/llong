# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def func(left, right):
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(val=nums[mid])
                node.left, node.right = func(left, mid - 1), func(mid + 1, right)
                return node

        return func(0, len(nums) - 1)