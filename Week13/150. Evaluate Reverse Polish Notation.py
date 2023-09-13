class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for item in tokens:
            if item != "+" and item != '-' and item != '*' and item!= '/':
                stack.append(int(item))    
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if item == "+":
                    ans  = op1 + op2
                elif item == '-':
                    ans = op1 - op2
                elif item == '*':
                    ans = op1 * op2
                elif item == "/":
                    ans = int(op1/op2)
                    

                stack.append(ans)
   
        return stack[0]


        
