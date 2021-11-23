from page11.leet501_find_mode import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        header = TreeNode(0)
        cur = header
        def visit(node):
            nonlocal cur
            if node.left is not None:
                visit(node.left)
            cur.right = node
            cur =cur.right
            cur.left = None
            if node.right is not None:
                visit(node.right)
        visit(root)
        return header.right

if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    solution.increasingBST(root)