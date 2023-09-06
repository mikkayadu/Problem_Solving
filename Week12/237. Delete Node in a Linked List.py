class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # prev = node
        # while prev and prev.next:
        #     prev.val = prev.next.val
        #     prev1 = prev
        #     prev = prev.next
        # prev1.next = None
        
        # prev = node
        
        # prev.val =prev.next.val
        # prev.next = prev.next.next
        node.val = node.next.val
        node.next = node.next.next
