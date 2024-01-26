# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        sorted = ListNode()
        
        second = sorted
        while first:
            while second.next and first.val > second.next.val:
                second = second.next
            temp = second.next
            firstnext = first.next
            second.next = first
            second.next.next = temp
            first = firstnext
            second = sorted 

        return (sorted.next)
        


        