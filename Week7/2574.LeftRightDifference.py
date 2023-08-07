def leftRightDifference( nums: list[int]) -> list[int]:
    answer = []
    
    for r in range(len(nums)):
        ans = abs(sum(nums[:r]) - sum(nums[r+1: ]))
        answer.append(ans)
    return answer
