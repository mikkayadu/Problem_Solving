class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        res = []
        end, start = 0, 0
        for i in range(len(s)):
            end = max(end, s.rindex(s[i]))

            if i == end:
                res.append(end - start+1)
                start = i + 1
        return res