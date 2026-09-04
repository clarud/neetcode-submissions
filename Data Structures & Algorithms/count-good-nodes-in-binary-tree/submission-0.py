# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque()
        q.append((root, root.val))
        while q:
            curr, maxval = q.popleft()
            if not curr:
                continue
            if curr.val >= maxval:
                count += 1
            maxval = max(maxval, curr.val)
            q.append((curr.left, maxval))
            q.append((curr.right, maxval))
        return count