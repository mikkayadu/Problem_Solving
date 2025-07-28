# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)

        def solve(node):
            if not node:
                return TreeNode(val)
            
            if val > node.val:
                ans = solve(node.right)
                if ans:
                    node.right = ans
                    
            else:
                ans = solve(node.left)
                if ans:
                    node.left = ans
        solve(root)
        return root
            
        