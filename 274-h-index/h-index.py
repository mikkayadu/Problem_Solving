class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, 1000
        n = len(citations)
        citations.sort()

        while l < r : 
            mid = (l + r)//2
            count = 0
            for i in range(n):
                if citations[i] >= mid:
                    count += 1
            if count < mid:
                r = mid


            else:
                l = mid + 1
            
        return l-1
    
                
            
             