class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def is_valid_state(state):
            # check if it is a valid solution
            if len(state) == len(nums):
                return True
            return False

        def get_candidates(state):
            lst = []
            start = max(state) if state else 1
            for i in nums:
                if i not in state:
                    lst.append(i)
            return lst

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                return

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.remove(candidate)

        def solve():
            solutions = []
            state = []
            search(state, solutions)
            return solutions
        
        return solve()

        
