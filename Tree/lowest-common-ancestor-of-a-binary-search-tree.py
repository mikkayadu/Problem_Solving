# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        if (root.val >= p.val and root.val <=q.val) or (root.val <= p.val and root.val >= q.val):
            return root
        elif root.val < p.val :
            ans = self.lowestCommonAncestor(root.right,p,q)
        elif root.val > q.val:
           ans =  self.lowestCommonAncestor(root.left, p, q)
        return ans