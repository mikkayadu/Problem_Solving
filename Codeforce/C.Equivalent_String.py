memo = {}
def solve(a, b):
    if (a,b) in memo:
        return memo[a,b]
    if len(a)%2 == 1:
        return a == b
    
    half = len(a)//2
    a1, a2 = a[:half], a[half:]
    b1, b2 = b[:half], b[half:]
 
    memo[a,b] = (solve(a1, b1) and solve(a2, b2)) or  (solve(a1, b2) and solve(a2, b1))
    return memo[a,b]
 
s1 = input()
s2 = input()    
ans = solve(s1, s2)
 
print("YES" if ans else "NO")
