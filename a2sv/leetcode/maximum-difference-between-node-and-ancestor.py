class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def find(node, minimum, maximum):
            nonlocal ans

            if not node:
                return

            ans = max(ans, abs(node.val - minimum), abs(node.val - maximum))
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)

            find(node.left, minimum, maximum)
            find(node.right, minimum, maximum)

        find(root, root.val, root.val)
        return ans