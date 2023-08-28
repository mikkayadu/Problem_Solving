from collections import Counter
def maximumSubarraySum(nums: list[int], k: int) -> int:
    cur_string = Counter(nums[:k])
    size = len(cur_string)
    cur_sum = sum(nums[:k]) 
    max_sum = cur_sum if size == k else 0
    
    for r in range(k, len(nums)):
        if nums[r] not in cur_string:
            size+=1
        cur_string[nums[r]] = cur_string.get(nums[r], 0) + 1
        

        cur_sum += nums[r]

        out = nums[r-k]

        cur_string[out] -=1
        cur_sum -= out
        

        if cur_string[out] == 0:
            cur_string.pop(out)
            size-=1
        
        if size == k and cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum
        


print(maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3))
