class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1 = list(s1);s1.sort()
        string = list(s2)
        start = string[:k]; 
        if s1 == sorted(start):
            return True

        for i in range(k, len(string)):
            start.append(string[i])
            start = start[1:]
            
            if sorted(start)== s1:
                return True
        return False
