n = int(input())
a = list(map(int, input().split()))

def solve():
    odd = [num for num in a if num%2 != 0]
    even = [num for num in a if num%2 == 0]
    if len(odd) == 0 or len(even) == 0:
        return a
    
    a.sort()
    return a

print(*solve())


    
