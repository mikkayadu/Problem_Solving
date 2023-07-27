class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        tracker = len(arr) -1
        while tracker >0:
            flip_index = arr.index(max(arr[:tracker+1]))
            ans.append(flip_index +1)
            
            arr = arr[:flip_index+1][::-1] + arr[flip_index+1:]
            arr = arr[:tracker+1][::-1] + arr[tracker+1:]
            ans.append(tracker+1)
            tracker-=1
        return ans