from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        next_q = [root]
        next_level = 1
        while len(next_q) > 0:
            q = next_q[::-1]
            next_q = []
            vals = []
            for node in q:
                vals.append(node.val)
                if next_level % 2 == 0:
                    if node.right is not None:
                        next_q.append(node.right)
                    if node.left is not None:
                        next_q.append(node.left)
                else:
                    if node.left is not None:
                        next_q.append(node.left)
                    if node.right is not None:
                        next_q.append(node.right)
            ans.append(vals)
            next_level += 1
        return ans

if __name__=="__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(19)
    node5= TreeNode(15)
    node6 = TreeNode(7)
    node1.left = node2
    node2.right = node4
    node1.right = node3
    node3.left = node5
    node3.right = node6
    solution = Solution()
    print(solution.zigzagLevelOrder(node1))
