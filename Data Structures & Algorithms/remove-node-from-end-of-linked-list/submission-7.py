# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        first = slow = fast = head
        # n is the length
        for i in range(n + 1):
            if fast == None:
                return first.next
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        if slow.next:
            slow.next = slow.next.next
        return first