# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = 0

        mn = min (p.val , q.val)
        mx = max (p.val , q.val)
        def helper(root , mn , mx ):
            nonlocal ans
            if mn <= root.val and  root.val <= mx:
                
                ans = root
                return 
            elif root.val < mx :
                helper(root.right , mn , mx)
            else:
                helper(root.left , mn ,mx)
            
        helper(root, mn ,mx )
        
        return ans 

        