class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less = ListNode()
        dummy_more = ListNode()
        myvarless = dummy_less
        myvarmore =dummy_more
        
        cur_node = head

        while cur_node:
            if cur_node.val < x:
                myvarless.next = cur_node
                myvarless = myvarless.next
            else:
                myvarmore.next = cur_node
                myvarmore = myvarmore.next
            cur_node = cur_node.next
        
        myvarmore.next = None
        myvarless.next = dummy_more.next
        return dummy_less.next
