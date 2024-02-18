# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
       
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        
        part_size = length // k
        extra = length % k
        
        
        parts = []
        curr = head
        prev = None
        for i in range(k):
            parts.append(curr)
            
            
            size = part_size
            if extra > 0:
                size += 1
                extra -= 1
            
            
            for j in range(size):
                prev = curr
                curr = curr.next
            
            
            if prev:
                prev.next = None
        
        return parts