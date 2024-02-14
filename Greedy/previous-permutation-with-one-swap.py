class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        increase = None

        for r in range(len(arr)-1,  0,-1):
            if arr[r] < arr[r-1]:
                increase = r-1
                break
        
        if increase is None:
            return arr

        small = None
        for r in range(len(arr)-1, increase , -1):
            if  arr[r] < arr[increase]:
                small = r
                
                while r > increase + 1 and arr[r-1] == arr[r]:
                    r-=1
                    small = r
                    
                break
        if  small:
            arr[increase], arr[small] = arr[small], arr[increase]
        return arr