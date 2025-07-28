class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxi = 0
        answer = 0
        for val in nums:
            maxi |= val

        
        def is_valid(state):
            nonlocal maxi
            ans = 0
            for val, index in state:
                ans |= val

            if ans == maxi:
                return True
            return False

        
        def get_candidate(state):
            start = state[-1][1] if state else -1
            lst = []

            for i in range(start+1, len(nums)):
                lst.append([nums[i], i])

            return lst

        
        def search(state):
            nonlocal answer
            if is_valid(state):
                answer += 1
            
            for candidate in get_candidate(state):
                state.append(candidate)
                search(state)
                state.pop()
        

        search([])

        
        return answer


