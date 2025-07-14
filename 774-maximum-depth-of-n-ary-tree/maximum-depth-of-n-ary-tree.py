"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0
            
        def dfs(node):
            if not node:
                return 0

            maxi = 0
            for child in node.children:
                maxi = max(1 + dfs(child), maxi)

            return maxi 

        return dfs(root) +1
        