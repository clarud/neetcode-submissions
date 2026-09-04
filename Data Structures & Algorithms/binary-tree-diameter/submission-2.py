# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # parent node has 1 + diameter of child node
        self.max_diameter = -float("inf")
        def diameter(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)
        diameter(root)
        return self.max_diameter
