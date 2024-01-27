# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0 
        dummy = ListNode(0)
        dummy.next = head 
        left = dummy  
        right = dummy 
        while right.next:
            
            if count >= n:
                left = left.next

            right = right.next 
            count += 1
        left.next = left.next.next if left.next else None 
        return dummy.next 


        