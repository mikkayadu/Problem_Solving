def productExceptSelf( nums: list[int]) -> list[int]:
    n = len(nums)
    prefix_product = [0] * (n+1)
    prefix_product[0] = 1
    r_prefix  = [0] * (n+1)
    r_prefix[0] =1
    res = []

    for r in range(1,len(prefix_product)):
        prefix_product[r] = prefix_product[r-1] * nums[r-1]

    nums.reverse()
    for r in range(1, len(r_prefix)):
        r_prefix[r]  = r_prefix[r-1] * nums[r-1]
    
    r_prefix.reverse()

    for i in range(1, len(nums)+1):
        res.append(r_prefix[i] * prefix_product[i-1])
    
    return res

    




print(productExceptSelf([-1,1,0,-3,3]))
