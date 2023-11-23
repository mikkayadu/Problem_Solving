# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Check:
#     def __init__(self,lists):
#         self.lists = lists
        
#     def __lt__(self, other):
#         return self.node.val < other.node.val
            
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        heap = []
        dummy=tail = ListNode()

        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))
        heapify(heap)
        

        while heap:
            if heap[0] == None:
                heappop(heap)
            else:
                dummy.next = heap[0][2]
                if heap[0][2] and heap[0][2].next:
                    store = (heap[0][2].next.val, heap[0][1], heap[0][2].next)
                else:
                    store = None
                heappop(heap)
                if store:
                    heappush(heap, store)
                dummy = dummy.next

            
        return tail.next

        