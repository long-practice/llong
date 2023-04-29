# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack.append(head)
            head = head.next

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]

        return stack[0]