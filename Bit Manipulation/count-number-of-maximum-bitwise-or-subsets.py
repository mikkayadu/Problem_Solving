class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        maxi = nums[0]
        for i in range(1, len(nums)):
            maxi |= nums[i]


        def is_valid(state):
            if state :
                ans = 0
                for num, i in state:
                    ans |= num
                if ans == maxi :
                    return True
            return  False
            
        
        def get_candidate(state):
            lst = []
            start = -1 if not state else state[-1][1]
            for i in range(start+1, len(nums)):
                lst.append((nums[i], i))
            
            return lst

        def search(state):
            nonlocal count
            if is_valid(state):
                count += 1
            
            for candidate in get_candidate(state):
                state.append(candidate)
                search(state)
                state.pop()
                
        
        def solve():
            state = []
            search(state)
        
        solve()
        return count
                
            
        