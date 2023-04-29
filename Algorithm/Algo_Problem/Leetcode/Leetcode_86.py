# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_x, greater_than_x = [], []

        curr = head
        while curr:
            if curr.val < x:
                less_than_x.append(curr)
            else:
                greater_than_x.append(curr)
            curr = curr.next

        node_list = less_than_x + greater_than_x
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]

        if node_list:
            node_list[-1].next = None

        return node_list[0] if node_list else None
