class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        count = 0 ; ans = None
        
        def get_candidates(state):
            lst = []
            myset = set(state)
            for i in range(1,  n+1):
                if i not in myset:
                    lst.append(i)

            return lst

            

        def search(state):
            nonlocal count

            if len(state) == n:
                count +=1
                
            
     
            for candidate in get_candidates(state):
                state.append(candidate)
                search(state)
                if count == k:
                    return "".join(list(map(str,state.copy())))
                state.pop()
            
        
           
        state = []

        return search(state)
