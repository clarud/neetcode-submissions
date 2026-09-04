# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            def helper(node1, node2):
                if node1 is None and node2 is None:
                    return True
                elif node1 is None or node2 is None:
                    return False             
                if node1.val != node2.val:
                    return False
                return helper(node1.left, node2.left) and helper(node1.right, node2.right)
            return helper(p, q)
        
        def helper(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if isSameTree(root, subRoot):
                return True
            return helper(root.left) or helper(root.right)
        
        return helper(root) 