# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Symmetric(leftroot , rightroot):
            if not leftroot and  not rightroot:
                return True 
            if (not leftroot and rightroot) or (not rightroot and leftroot):
                return False
            if leftroot and rightroot and leftroot.val != rightroot.val:
                return False
            return Symmetric(leftroot.left , rightroot.right) and Symmetric(leftroot.right , rightroot.left)
        return Symmetric(root.left , root.right)
        