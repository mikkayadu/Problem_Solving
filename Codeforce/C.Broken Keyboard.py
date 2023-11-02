t = int(input())
 
def solve():
    s = input()
    ans = set()
    if len(s) == 1:
        return s
    s += '1'
    l, r = 0, 1
 
    while r<len(s):
        if s[l] == s[r]:
            r += 1
        else:
            if (r-l) % 2 != 0:
                ans.add(s[l])
            l = r
            r +=1 
    return "".join(sorted(ans))
 
for _ in range(t):
    print(solve())
