# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        while l1 or l2 or carry:
            tmp = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry
            carry = tmp // 10
            node = ListNode(tmp % 10, prev)
            prev = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        last = None
        while prev:
            tmp = prev.next
            prev.next = last
            last = prev
            prev = tmp

        return last