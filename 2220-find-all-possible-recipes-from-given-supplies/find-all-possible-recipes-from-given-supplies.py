class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        n = len(ingredients)
        adj_list = defaultdict(list)
        edge_count = defaultdict(int)

        for i in range(n):
            for ingredient in ingredients[i]:
                adj_list[ingredient].append(recipes[i])
                edge_count[recipes[i]] += 1
        
        print("adj_list", adj_list)
        print("edge_count", edge_count)

        queue = deque(supplies)
        ans = []


        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                for nei in adj_list[node]:
                    edge_count[nei] -= 1

                    if edge_count[nei] == 0:
                        ans.append(nei)
                        queue.append(nei)

        return ans


        