class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur_node = head
        slow, fast = cur_node, cur_node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
       
        return False
