class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mappings = {
            "2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
            "7":"pqrs", "8":"tuv", "9":"wxyz"
        }

        lst = [list(mappings[let]) for let in digits]
        
        def is_valid(state):
            if len(state) ==len(digits):
                return True
            return False
        
        def get_candidate(state):
            index = state[-1][1] if state else -1
            arr = []

            ans = lst[index + 1]
            for i in range(len(ans)):
                arr.append((ans[i], index + 1))
            return arr

        
        def search(state, solutions):
            if is_valid(state):
                solutions.append(state.copy())
                return 

            for candidate in get_candidate(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()

        

        def solve():
            state = []
            solutions  = []
            search(state, solutions)
            return solutions

        solutions = solve()

        ans = []
        for arr in solutions:
            string = ""
            for let in arr:
                string += let[0]
            ans.append(string) if string else ""
        
        return ans
        