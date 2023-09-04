class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        elems = []
        elems2 = []
        self.head = head
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.val)
            cur_node = cur_node.next
       

        cur_node = self.head
        prev = None

        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt

        cur_node = prev
        while cur_node:
            elems2.append(cur_node.val)
            cur_node = cur_node.next
        
        if elems == elems2:
            return True
        return False
