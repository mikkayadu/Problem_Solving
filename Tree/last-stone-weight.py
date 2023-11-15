class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * val for val in stones]
        heapify(stones)
        while len(stones) >=2:
            
            y = heappop(stones)
            x = heappop(stones)
            print(stones)

            if x != y:
                heappush(stones,  (y - x))
        return -1 * stones[0] if stones else 0
            
            