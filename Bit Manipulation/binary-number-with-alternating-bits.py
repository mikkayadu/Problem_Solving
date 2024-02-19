class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length = n.bit_length()

        k = 1
        while k < length:
            print(" n & (1<<k)",  n & (1<<k))
            print("n&(1<<k-1)", n&(1<<k-1))
            if( n & (1<<k) != 0  and  n&(1<<k-1)!= 0) or ( n & (1<<k) == 0  and  n&(1<<k-1)== 0):
                return False
            else:
                k += 1
        return True

       



        