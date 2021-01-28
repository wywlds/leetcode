from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        max_count = 0
        max_vals = []
        last_val = None
        cur_count = 0

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            val = node.val
            if val != last_val:
                cur_count = 1
                last_val = val
            else:
                cur_count += 1
            if cur_count > max_count:
                max_vals = [val]
                max_count = cur_count
            elif cur_count == max_count:
                max_vals.append(val)
            node = node.right
        return max_vals

if __name__=="__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node1.right = node2
    node2.left = node3
    solution = Solution()
    print(solution.findMode(node1))