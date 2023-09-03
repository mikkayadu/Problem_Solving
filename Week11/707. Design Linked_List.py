class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size or index <0:
            return -1
        cur_node = self.head
        for i in range(index):
            cur_node = cur_node.next
        return cur_node.value
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0 , val)
        
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index <0:
            return 
        cur_node = self.head
        new_node  = Node(val)
        if index == 0:
            new_node.next = cur_node
            self.head = new_node
        else:

            for i in range(index-1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
        self.size +=1
        
        

    def deleteAtIndex(self, index: int) -> None:
        cur_node = self.head
        if index >= self.size or index <0:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index -1):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
        self.size -=1

    def prints(self):
        elems = []
        cur_node = self.head
        for i in range(self.size):
            elems.append(cur_node.value)
            cur_node = cur_node.next
        return elems
