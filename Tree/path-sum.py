# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root, targetSum):
            if not root:
                print("Im over here")
                print(targetSum)
                return False
                
            targetSum -= root.val

            if not root.right and not root.left:
                return targetSum == 0
            

            
            
            return solve(root.left, targetSum) or solve(root.right, targetSum)

        
        
        return solve(root, targetSum)
        
        
        
        
        

        
        
        
        
        
        
        
        