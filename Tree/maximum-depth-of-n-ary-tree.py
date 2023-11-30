"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        height = 0
        def dfs(root , count):
            nonlocal height
            if not root:
                height = max(count, height)
                return
            if not root.children:
                height = max(count+1, height)
                return

            for node in root.children:
                dfs(node, count+1)

        dfs(root, 0)
        return height

            

        



        


                
            
            
            
                

                
            
        