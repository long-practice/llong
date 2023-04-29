# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()

        dummy = curr = ListNode(-1e5 - 1)
        for n in arr:
            node = ListNode(n)
            curr.next = node
            curr = node

        return dummy.next

