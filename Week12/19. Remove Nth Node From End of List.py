# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        head = dummy_node

        right = head
        n +=1
        while n:
            right = right.next
            n -=1
        left = head

        while right:
            right = right.next
            left = left.next
        left.next= left.next.next
        
        
        return head.next

        
