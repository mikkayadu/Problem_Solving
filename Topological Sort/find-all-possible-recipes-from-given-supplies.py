class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_list = defaultdict(list)
        edge_count = defaultdict(int)
        supplies = set(supplies)
        ans = []
        for i in range(len(recipes)):
            for ingred in ingredients[i]:
                adj_list[ingred].append(recipes[i])
                edge_count[recipes[i]] += 1
        print("edge_count", edge_count)
        
        for key, value in adj_list.items() :
            if edge_count[key] == 0:
                ans.append(key)
        print("adj_list", adj_list)
        queue = deque(ans)
        print("ans", ans)
        res = []
        

        while queue:
            for i in range(len(queue)):
                node  = queue.popleft()
                
                
                if node in supplies:
                    for neighbour in adj_list[node]:
                        edge_count[neighbour] -= 1

                        if edge_count[neighbour] == 0:
                            queue.append(neighbour)
                            res.append(neighbour)
                            if neighbour not in supplies: supplies.add(neighbour)
                            
        return res
                    
            
        


        

        