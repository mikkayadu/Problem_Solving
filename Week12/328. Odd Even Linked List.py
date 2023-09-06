# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd = ListNode()
        dummy_even = ListNode()
        odd_ptr = dummy_odd
        even_ptr = dummy_even

        cur_node = head
        while cur_node and cur_node.next:
            
            odd_ptr.next= cur_node
            odd_ptr = odd_ptr.next

            even_ptr.next  = cur_node.next
            even_ptr = even_ptr.next
            

            cur_node = cur_node.next.next
        if cur_node:
            odd_ptr.next = cur_node
            odd_ptr = odd_ptr.next
        
       
        even_ptr.next = None
        odd_ptr.next = dummy_even.next
        return dummy_odd.next
