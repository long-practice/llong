# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        data_ls = []

        def preorder(node):
            if node:
                data_ls.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                data_ls.append('')

        preorder(root)
        return ','.join(data_ls)

    def deserialize(self, data):
        data_q = deque(data.split(','))

        def create_tree():
            num = data_q.popleft()
            if num:
                node = TreeNode(int(num))
                node.left = create_tree()
                node.right = create_tree()
                return node
            return None

        root = create_tree()
        return root