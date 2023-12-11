class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        n = len(nums)
        count = 0

        for i in range(n):
            l, r = i + 1, n - 1
            min_j, max_j = n, -1

            # Binary search to find minimum j such that nums[i] + nums[j] >= lower
            while l <= r:
                mid = (l + r) // 2
                if sorted_nums[i][0] + sorted_nums[mid][0] >= lower:
                    min_j = min(min_j, mid)
                    r = mid - 1
                else:
                    l = mid + 1

            l, r = i + 1, n - 1

           
            while l <= r:
                mid = (l + r) // 2
                if sorted_nums[i][0] + sorted_nums[mid][0] <= upper:
                    max_j = max(max_j, mid)
                    l = mid + 1
                else:
                    r = mid - 1

            
            if min_j <= max_j:
                count += max_j - min_j + 1

        return count

