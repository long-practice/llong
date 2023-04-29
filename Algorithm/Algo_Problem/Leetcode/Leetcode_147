# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-5001, next=head)

        pivot_prev, pivot = head, head.next
        while pivot:
            prev, curr = dummy, dummy.next

            while curr.val < pivot.val:
                prev, curr = prev.next, curr.next

            if pivot != curr:
                node = ListNode(val=pivot.val)
                prev.next, node.next = node, curr
                pivot_prev.next = pivot = pivot.next
            else:
                pivot_prev, pivot = pivot_prev.next, pivot.next

        return dummy.next