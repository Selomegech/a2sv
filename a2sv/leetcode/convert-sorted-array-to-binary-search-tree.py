# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(l , r):
            if l>r:
                return None 
            
            mid = (l+r)//2
            x = TreeNode(nums[mid])

            x.left = divide(l , mid-1)
            x.right = divide(mid+1 , r)
            return x
        
        return(divide(0 , len(nums)-1))
        