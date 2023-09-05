class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {-102:2}
        cur_node = head

       

        while cur_node and cur_node.next:
        
            hashmap[cur_node.val] = hashmap.get(cur_node.val, 0) +1

            if cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        if cur_node!= None:
            cur_node.next = ListNode(-102)
            hashmap[cur_node.val] = hashmap.get(cur_node.val, 0) +1
        
        
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        cur_node = head
        ala = head
        print(head)

        while cur_node and cur_node.next:
            if hashmap[cur_node.next.val] > 1:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        cur_node = None
        return head.next
