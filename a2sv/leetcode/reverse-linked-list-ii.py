# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy 
        count = 0

        while  left-1  != count:
            curr = curr.next
            count += 1

        curr_prev = curr
        left_node = curr.next
        curr_node = left_node

        size = right - left +1

        while size:
            temp = curr_node.next 
            curr_node.next = curr_prev
            curr_prev = curr_node
            curr_node = temp
            size -= 1

        left_node.next = temp 
        curr.next = curr_prev 
        return dummy.next 







        
            
        

        