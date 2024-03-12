# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        store = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            store.append(node.val)
            dfs(node.right)
        dfs(root)
        def solve( left = 0 , right = len(store) - 1):
            if left > right :
                return None
            mid = (left + right) // 2
            node = TreeNode(store[mid])
            node.left = solve(left , mid -1)
            node.right = solve(mid+1 , right)

            return node
        return solve()
        