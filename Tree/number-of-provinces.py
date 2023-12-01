class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node, adj_list, visit):
            if not node:
                return
            if node in visit:
                return 
            
            visit.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour, adj_list, visit )
            
        
        count = 0
        visit = set()
        adj_list = defaultdict(list)
        
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    adj_list[row+1].append(col+1)
        
        
        for node in adj_list:
            if node not in visit:
                dfs(node, adj_list, visit)
                count +=1
                
        return count
        
        
        