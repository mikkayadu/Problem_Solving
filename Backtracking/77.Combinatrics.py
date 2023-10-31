class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def is_valid_state(state):
        # check if it is a valid solution
            if len(state) == k:
                return True
            return False

        def get_candidates(state):
            lst = []
            start = max(state) if state else 1
            for i in range(start, n+1):
                if i not in state:
                    lst.append(i)
            return lst

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(list(state.copy()))
                return

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        def solve():
            solutions = []
            state = set()
            search(state, solutions)
            return solutions
        return solve()
        
