class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mymoney = defaultdict(int)

        for i in range(len(bills)):
            mymoney[bills[i]] += 1
            change = bills[i] - 5
            
            if change == 0:
                continue
            
            if change == 5 :
                if mymoney[change] > 0:
                    mymoney[change] -= 1
                else:
                    return False
            else:
                if change == 15:
                    if mymoney[10] > 0 and mymoney[5]>0:
                        mymoney[10] -=1
                        mymoney[5] -=1
                    elif  mymoney[5] >= 3:
                        mymoney[5] -=3
                    else:
                        return False
        return True
                    
                        
                     