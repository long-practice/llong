# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent, r_node = self.search(None, root, key)

        if r_node:
            c_children = self.count_children(r_node)
            if c_children == 0:
                if parent:
                    if r_node.val < parent.val:
                        parent.left = None
                    else:  # r_node.val > parent.val
                        parent.right = None
                else:
                    root = None

            elif c_children == 1:
                if r_node.left:
                    child = r_node.left
                else:  # r_node.right:
                    child = r_node.right
                if parent:
                    if parent.val > r_node.val:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    root = child

            else:  # c_children == 2:
                p, successor = r_node, r_node.right
                while successor.left:
                    p, successor = successor, successor.left
                r_node.val = successor.val

                if p.val > successor.val:
                    p.left = successor.right
                else:
                    p.right = successor.right
        return root


    def search(self, parent, curr, key):
        if curr:
            if curr.val == key:
                return parent, curr
            elif curr.val > key:
                return self.search(curr, curr.left, key)
            else:  # curr.val < key:
                return self.search(curr, curr.right, key)
        return None, None


    def count_children(self, node):
        count = 0
        if node.left:
            count += 1
        if node.right:
            count += 1
        return count