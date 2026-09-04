# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.num = k
        self.ans = None
        def helper(node):
            if not node or self.ans is not None:
                return
            helper(node.left)
            if self.ans is not None:
                return
            self.num -= 1
            if self.num == 0:
                self.ans = node
                return
            helper(node.right)
        helper(root)
        return self.ans.val