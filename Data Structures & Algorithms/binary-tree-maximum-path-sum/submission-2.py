# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -float("inf")
        def helper(node):
            if not node:
                return 0
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            max_with_root = left + right + node.val
            self.max_path = max(max_with_root, self.max_path)
            return max(left + node.val, right + node.val, node.val)
        helper(root)
        return self.max_path

