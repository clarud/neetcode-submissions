# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        if p.val <= q.val:
            left = p
            right = q
        else:
            left = q
            right = p
        while not (lca.val >= left.val and lca.val <= right.val):
            if lca.val <= left.val and lca.val <= right.val:
                lca = lca.right
            if lca.val > left.val and lca.val > right.val:
                lca = lca.left
        
        return lca