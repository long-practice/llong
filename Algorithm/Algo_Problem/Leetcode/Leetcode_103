# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        elements = {}
        if root:
            q = deque([(root, 1)])
            while q:
                node, depth = q.popleft()
                if node:
                    elements[depth] = elements.get(depth, []) + [node.val]
                    q.append((node.left, depth + 1))
                    q.append((node.right, depth + 1))

        zigzag_traversal = [[x for x in elements[k] if x != None] for k in elements.keys()]
        return [zigzag_traversal[i] if not i % 2 else zigzag_traversal[i][::-1] for i in range(len(zigzag_traversal))]