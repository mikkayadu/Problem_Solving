# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mid(head):
            slow = head
            fast = head.next
            while fast and fast.next :
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left, right):
            dummy = tail = ListNode()

            while left and right:
                if left.val < right.val:
                    dummy.next = left
                    left = left.next
                else:
                    dummy.next = right
                    right = right.next
                dummy = dummy.next
            
            if left:
                dummy.next  = left
            if right:
                dummy.next = right
            return tail.next
        


        def solve(head):
            
            if not head or head.next == None:
                return head

            left = head
            right = mid(head)
            temp = right.next
            right.next = None
            right = temp

            left = solve(left)
            right = solve(right)

            return merge(left, right)
        
        return solve(head)

            
            


            


        