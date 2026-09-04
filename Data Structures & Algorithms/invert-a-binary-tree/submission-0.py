# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node: Optional[TreeNode]):
        if not node:
            return
        else:
            self.helper(node.left)
            self.helper(node.right)
            tmp = node.left
            node.left = node.right
            node.right = tmp
            return

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root
    