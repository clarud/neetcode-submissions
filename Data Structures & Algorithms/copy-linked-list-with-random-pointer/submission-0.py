"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodedict = {}
        trav = head
        def recur(node):
            if not node:
                return None
            if node in nodedict:
                return nodedict[node]
            new = Node(node.val)
            nodedict[node] = new
            new.next = recur(node.next)
            new.random = recur(node.random)
            return new
        new = recur(trav)
        return new