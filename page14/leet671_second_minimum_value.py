class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import heapq
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        q = [float("-inf"), float("-inf")]
        def find(node):
            if node:
                -node.val not in q and heapq.heappushpop(q, -node.val)
                find(node.left)
                find(node.right)
        find(root)
        return q[0] == -float("inf") and -1 or -q[0]


if __name__=="__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    solution = Solution()
    print(solution.findSecondMinimumValue(node1))


