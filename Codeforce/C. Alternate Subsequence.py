t = int(input())
def check(mylist:list):
    if mylist[-1] < 0 :
        mylist.append(7)
    else:
        mylist.append(-7)
    l, r = 0, 1
    ans  = 0
    while r<len(mylist) :
        if (mylist[r] < 0 and mylist[l] > 0):
            ans += max(mylist[l:r])
            l = r
        
 
        elif  (mylist[r] > 0 and mylist[l] < 0):
            ans += max(mylist[l: r])
            l = r
        else:
            r+=1
           
        
    return ans
    
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    print(check(arr))
