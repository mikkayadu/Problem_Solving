class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        twos = ''
        for i in range(len(binary)):
            if binary[i] == "1":
                twos+= "0"
            else:
                twos+="1"
        return int(twos, 2)
            
        
