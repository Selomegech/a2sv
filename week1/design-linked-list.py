class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None 


class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        

    def get(self, index: int) -> int:

        if self.length <= index:
            return -1 

        cur = self.head
        
        for i in range(index):
            cur = cur.next 
           
        return cur.val
            
            

    def addAtHead(self, val: int) -> None:
        self.length += 1 
        newnode = Node(val)

        if not self.head:
            self.head = newnode 
            return

        cur = self.head
        newnode.next = self.head
        self.head = newnode
        

    def addAtTail(self, val: int) -> None:
        self.length += 1 
        cur = self.head
        newnode = Node(val)
        if not self.head:
            self.head = newnode 
            return  

        while cur and cur.next :
            cur = cur.next
        cur.next = newnode 

    def addAtIndex(self, index: int, val: int) -> None:
        if self.length < index:
            return 

        cur = self.head
        newnode = Node(val)

        if index == 0:
            self.addAtHead(val)
            return 
        self.length += 1
        for i in range(index-1):
            cur = cur.next
            


        newnode.next = cur.next
        cur.next = newnode

        

    def deleteAtIndex(self, index: int) -> None:
        if self.length <= index:
            return 
        self.length -= 1
        cur = self.head
        if index == 0:
            self.head = self.head.next
            return 

        for i in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)