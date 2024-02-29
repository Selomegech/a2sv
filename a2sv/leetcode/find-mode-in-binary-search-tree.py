class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = {}
        lst = []
        maxi = 0
        def find(root):
            if not root :
                return 
            if root.val not in d:
                d[root.val] = 1
            if root.val in d:
                d[root.val] += 1
            find(root.right)
            find(root.left)
        find(root)
        nums = list(d.values())
        print(nums)
        maxi = max(nums)
        print(maxi)
        for key , val in d.items():
            if val == maxi:
                lst.append(key)
        return (lst)
