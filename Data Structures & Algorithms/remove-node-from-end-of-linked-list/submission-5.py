# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return 0
        index = 0
        start = trav = head
        while trav:
            trav = trav.next
            index += 1
        time = index - n
        trav = start
        i = 0
        while i < time - 1: 
            trav = trav.next
            i += 1
        if trav.next:
            if time == 0:
                start = trav.next
            else:
                trav.next = trav.next.next
        else:
            return None
        return start
        