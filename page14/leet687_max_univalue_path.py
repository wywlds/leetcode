class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        max_path = 0

        def path(node):
            nonlocal max_path
            if node is None:
                return 0
            path_num = 0
            sum_path_num = 0
            left_path = self.path(node.left)
            right_path = self.path(node.right)
            if node.left and node.val == node.left.val:
                path_num = left_path + 1
                sum_path_num += path_num
            if node.right and node.val == node.right.val:
                path_num = max(right_path + 1, path_num)
                sum_path_num += (right_path + 1)
            max_path = max(max_path, sum_path_num)
            return path_num
        path(root)
        return max_path


if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(5)
    node3 = TreeNode(5)
    node1.right = node2
    node2.right = node3
    solution = Solution()
    solution.longestUnivaluePath(node1)