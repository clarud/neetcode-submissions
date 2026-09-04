# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, -float("inf"), float("inf"))])

        while q:
            node, low, high = q.popleft()
            if not (low < node.val < high):
                return False

            if node.left:
                # left must be in (low, node.val)
                q.append((node.left, low, node.val))
            if node.right:
                # right must be in (node.val, high)
                q.append((node.right, node.val, high))

        return True