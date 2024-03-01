# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def list_out(root):
            if not root :
                return []
            return list_out(root.left) + [root.val] + list_out(root.right)

        tree_list = list_out(root)
        return tree_list[k-1]
