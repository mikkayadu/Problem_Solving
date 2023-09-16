class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) -1 
        #implementing bisect right
        while low<= high:
            mid = low + (high - low)//2


            if nums[mid] <= target :
                low = mid + 1
            else:
                high = mid -1
            
            
        ans2 =  low - 1 if low-1 >= 0 and len(nums) > low -1 and  nums[low-1] == target else -1
        

        low, high = 0, len(nums)-1
        while low<= high:
            mid = low + (high - low)//2

            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        print(high)
        ans1= high+1 if len(nums) > high + 1 and nums[high+1] == target else -1
        return [ans1, ans2]
            
        
        
