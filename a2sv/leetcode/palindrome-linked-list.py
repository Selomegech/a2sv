# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head 
        slow = fast = head 
        step = 0
        while fast and fast.next:
            step += 1
            slow = slow.next
            fast = fast.next.next
        right = None 
        if fast:
            right = slow.next
        else:
            right = slow

        prev = None
        for i in range(step):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        while right and prev:
            if right.val != prev.val:
                return False
            right = right.next
            prev = prev.next
        return True 
         


        