class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state, solutions):
            return True
    
        def get_candidate(state):
            lst = []
            start = nums.index(state[-1]) if state else -1
            for i in nums[start+1:]:
                lst.append(i)
            
            return lst

        def search(state, solutions):
            if is_valid_state(state, solutions):
                solutions.append(state.copy())
            
            for candidate in get_candidate(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()

        def solve():
            solutions = []
            state = []
            search(state, solutions)
            return solutions
        
        ans = solve()
        return ans

        
        
        
