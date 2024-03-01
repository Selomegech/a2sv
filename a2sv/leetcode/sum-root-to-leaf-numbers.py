# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def helper(dg , root):
            if not root:
                return ''
            if not root.left and not root.right:
                ans .append(int(dg + str(root.val)))
            helper(dg + str(root.val) , root.left)
            helper(dg + str(root.val) , root.right)
            
        helper('' , root)
        
        return (sum(ans))




        
        