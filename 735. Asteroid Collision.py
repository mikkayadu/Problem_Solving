class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        flag = True

        for r in range(len(asteroids)):
            while  flag:
                if stack and stack[-1] < 0:
                    if asteroids[r] > 0 or asteroids[r] < 0:
                        stack.append(asteroids[r])
                        flag = False
                    
                elif stack and stack[-1] > 0:
                    if asteroids[r] < 0  and abs(asteroids[r]) > stack[-1]:
                        stack.pop()

                    elif asteroids[r] < 0 and  abs(asteroids[r]) < stack[-1]:
                        flag = False
                    elif asteroids[r] > 0:
                        stack.append(asteroids[r])
                        flag = False
                    else:
                        stack.pop()
                        flag = False
                
                else:
                    stack.append(asteroids[r])
                    flag = False

            flag = True
        return stack
        
            
