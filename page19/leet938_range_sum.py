from page11.leet501_find_mode import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        ans = 0
        def search(node):
            if node is None:
                return
            nonlocal ans
            if low <= node.val <= high:
                ans += node.val
                search(node.left)
                search(node.right)
            elif node.val < low:
                search(node.right)
            else:
                search(node.left)
        search(root)
        return ans