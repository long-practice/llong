# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_node = None
        if head and head.next:
            next_node = head.next
        if head and next_node:
            next_node.next, head.next = head, self.swapPairs(next_node.next)
            return next_node
        return head