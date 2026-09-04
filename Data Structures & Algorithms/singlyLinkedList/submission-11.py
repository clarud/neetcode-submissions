class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    
    def get(self, index: int) -> int:
        # return value of ith node else return -1
        if not self.head:
            return -1
        if self.size < index + 1:
            return -1
        node = self.head
        for i in range(index):
            node = node.next
        return node.val
        

    def insertHead(self, val: int) -> None:
        # insert val at the head of the list
        if not self.head:
            self.head = ListNode(val)
            self.size += 1
            return
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        # insert at tail
        if not self.head:
            self.head = ListNode(val)
            self.size += 1
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        # remove ith node true when pass
        if self.size < index + 1:
            return False
        if self.size == 1:
            self.head = None
            self.size -= 1
            return True
        slow, fast = ListNode(0), self.head
        dummy = slow
        slow.next = fast
        for i in range(index):
            fast = fast.next
            slow = slow.next
        slow.next = fast.next
        self.size -= 1
        self.head = dummy.next
        return True

        

    def getValues(self) -> List[int]:
        # get all vals in a list
        res = []
        node = self.head
        while node:
            res.append(node.val)
            node = node.next
        return res
        
