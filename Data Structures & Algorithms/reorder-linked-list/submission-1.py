# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        tmp = slow
        back = slow = slow.next
        tmp.next = None

        last = reversal = slow
        pointed = None
        while reversal:
            if reversal.next == None:
                last = reversal
            tmp = reversal.next
            reversal.next = pointed
            pointed = reversal
            reversal = tmp
        front = head
        back = last
        # merge
        # arr1 = []
        # arr2 = []
        # while front:
        #     arr1.append(front.val)
        #     front = front.next
        # while back:
        #     arr2.append(back.val)
        #     back = back.next
        # print(f"{arr1} / {arr2}")
        while back and front:
            tmp = front.next
            tmp1 = back.next
            front.next = back
            back.next = tmp
            front = tmp
            back = tmp1
        return
        

        
