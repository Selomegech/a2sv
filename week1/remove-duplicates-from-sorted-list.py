# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        curr = head
        sortedd = curr
        temp = curr
        s =sortedd
        
        while curr:
            if curr.val != temp.val:
                
                sortedd.next = curr
                temp = curr 
                sortedd = sortedd.next
                
            curr = curr.next
            
        sortedd.next  = None 
        return s