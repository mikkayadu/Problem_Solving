class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        mylist = {}
        maximum = float('-inf')
        max_value = 0

        for src, dest in edges:
            mylist[src] = mylist.get(src, 0) + 1
            mylist[dest] = mylist.get(dest, 0) + 1
        print(mylist)
        
        
        for key, value in mylist.items():
            # print("key", key)
            # print("value", value)
            if value > maximum:
                maximum = value
                max_value = key
        return max_value

        