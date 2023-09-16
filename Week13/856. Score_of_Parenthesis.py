class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
    
        total = 0

        for paren in s:
            if  paren == '(':
                stack.append(0)
            else:
                value = stack.pop()
                value = 1 if value == 0 else value * 2
                
                if stack:
                    stack[-1] += value
                else: 
                    total += value
    
        return total
