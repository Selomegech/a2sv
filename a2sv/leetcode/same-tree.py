# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        def helper1(root):
            if root:
                ans1.append(root.val)
                helper1(root.left)
                helper1(root.right)
            if not root:
                ans1.append(None)
            return ans1 
        def helper2(root):
            if root:
                ans2.append(root.val)
                helper2(root.left)
                helper2(root.right)
            if not root:
                ans2.append(None)
            return ans2 
        
        
        return (helper1(p) == helper2(q))
        