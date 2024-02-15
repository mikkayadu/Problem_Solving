class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary =""; ans = x ^y
        while ans>0:
            binary += str(ans&1)
            ans >>=1
        return binary[::-1].count("1")
        