# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        visit = set([root])
        queue = deque([root])

        def dfs(root):
            while queue:
                values = []
                for i in range(len(queue)):
                    cur_node = queue.popleft()
                    if cur_node:
                        values.append(cur_node.val)
                        queue.append(cur_node.left)
                        queue.append(cur_node.right)
                if values:
                    ans.append(sum(values)/len(values))
        
        dfs(root)
        return ans



        
