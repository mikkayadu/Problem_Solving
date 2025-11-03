"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}
        def helper(node):
            if not node:
                return
                
            if node in visited:
                return visited[node]
            

            curNeighbours = []
            visited[node] = Node(node.val, curNeighbours)
            for nei in node.neighbors:
                neighbour = helper(nei)
                curNeighbours.append(neighbour)

            

            return visited[node]
        
        return helper(node) 