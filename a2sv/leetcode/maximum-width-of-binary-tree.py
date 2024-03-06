# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = {}

        def solve(root , level , col):
            if not root:
                return 
            if level not in ans:
                ans[level] = [col]
            else:
                ans[level].append(col)

            solve(root.left, level+1 , (2 * col)+1)
            solve(root.right, level+1 , (2 * col)+2)
        solve(root , 1 , 0)
        print(ans)
        maxi = 0
        for key , val in ans.items():
            if len(val) == 1:
                continue
            m = max(val) 
            n = min(val)
            maxi = max(maxi , m-n)

        return (maxi + 1)





        