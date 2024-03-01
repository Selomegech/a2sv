# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def zigzag(i , root):
            if len(res) <= i:
                res.append([root.val])
            else:
                res[i].append(root.val)
            i += 1
            if root.left:
                zigzag(i , root.left)
            if root.right:
                zigzag(i , root.right)
        if root:
            zigzag(0 , root)
        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()
        return res 
            
            