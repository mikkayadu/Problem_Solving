t = int(input())
 
def solve():
    n = int(input())
    a = input()
    arr = a.split("#")
    arr = [len(i) for i in arr]
    if max(arr) >= 3:
        return 2
    return a.count(".")
 
for _ in range(t):
    print(solve())
 
