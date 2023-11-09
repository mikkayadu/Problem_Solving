class Solution:
    def splitString(self, s: str) -> bool:
        def is_valid_state(state):
            if len("".join(state) ) == len(s) and check(state) :
                return True
            
            return False
        
        def get_candidate(state):
            lst = []
            start = len("".join(state)) if state else 0 
            rem = s[start:]
            for i in range(len(rem)):
                if not state or check([state[-1], int(rem[:i+1])]):
                    lst.append(rem[: i+1])
            
            return lst

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                return 
            
            for candidate in get_candidate(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()

        def solve():
            solutions = []
            state = []
            search(state, solutions)
            return solutions
        
        
        
        def check(lst):
            
            if len(lst) == 1:
                flag = False
            else:
                flag = True
            for i in range(len(lst)-1):
                if int(lst[i]) <= int(lst[i+1]) or abs(int(lst[i]) - int(lst[i+1])) != 1:
                    flag = False

            
            if   flag:
                
                return True
            return False
            
        return False if solve() == [] else True