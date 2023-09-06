# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l, r = left, right
        dummy_node = ListNode()
        dummy_node.next = head

        cur_node = dummy_node
        for _ in range(left-1):
            cur_node = cur_node.next

        left = cur_node
        left1 = cur_node.next
        
        #reversing linked list
        prev = None
        curr = left1

        for i in range(r-l+1):
            store = curr.next
            curr.next = prev
            prev = curr
            curr = store
            
        left.next = prev
        left1.next = curr
        return dummy_node.next
