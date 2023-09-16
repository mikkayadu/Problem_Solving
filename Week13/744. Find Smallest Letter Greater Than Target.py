class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if letters[-1] <= target:
            return letters[0]

        low, high  = 0, len(letters) -1

        while low <= high:
            mid = (low + high)//2

            if letters[mid] <= target:
                low = mid + 1
            
            else:
                high = mid -1
        return letters[low]

        


        
        
