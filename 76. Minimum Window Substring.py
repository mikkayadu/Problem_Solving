class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        ans = ""
        l = 0
        mydict = defaultdict(int)
        count = Counter(t)

        def contains(mydict, count):
            for c in count:
                if mydict[c] < count[c]:
                    return False
            return True

        for r in range(m):
            if s[r] in count:
                mydict[s[r]] += 1

            
            while contains(mydict, count):
                if ans == "" or (r - l + 1) < len(ans):
                    ans = s[l:r+1]

                if s[l] in mydict:
                    mydict[s[l]] -= 1
                l += 1

        return ans
        
