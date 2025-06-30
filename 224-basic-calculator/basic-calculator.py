class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        res = 0
        current_sign = 1
        i = 0

        while i < len(s):
            char = s[i]

            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char in ["+" , "-"]:
                res += current_sign * current_num
                current_num = 0
                current_sign = 1 if char == "+" else -1 
            
            elif char == "(":
                stack.append(res)
                stack.append(current_sign)
                res = 0
                current_sign = 1
            
            elif char == ")":
                res += current_sign * current_num
                current_num = 0
                current_sign = 1

                res *= stack.pop()
                res += stack.pop()

            i += 1

        res += current_sign * current_num
        return res

                



        