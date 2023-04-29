# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_ls, mid_ls, right_ls = [], [], []
        order = 1
        while head:
            if order < left:
                left_ls.append(head)
            elif order > right:
                right_ls.append(head)
            else:
                mid_ls.append(head)
            head = head.next
            order += 1

        node_ls = left_ls + mid_ls[::-1] + right_ls
        for i in range(len(node_ls) - 1):
            node_ls[i].next = node_ls[i + 1]
        node_ls[-1].next = None

        return node_ls[0]
