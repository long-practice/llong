# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root:
            nums = self.sort_tree(root, [])
            for i in range(len(nums) - 1):
                left, right = i, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == k:
                        return True
                    elif nums[left] + nums[right] > k:
                        right -= 1
                    else:
                        break
        return False

    def sort_tree(self, node, ls):
        if node:
            if node.left:
                ls = self.sort_tree(node.left, ls)
            ls.append(node.val)
            if node.right:
                ls = self.sort_tree(node.right, ls)
        return ls