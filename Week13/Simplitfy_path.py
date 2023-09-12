from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        mydeque = deque()
        path = path.split('/')
        

        for i in path:
            if len(mydeque) > 0 and i == "..":
                mydeque.pop()

            elif i!="" and i!= ".." and i!='.':
                mydeque.append(i)
        
        return '/' + '/'.join(mydeque)
        

