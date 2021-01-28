from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        node_queue = queue.Queue()
        layer_queue = queue.Queue()

        node_queue.put(root)
        layer_queue.put(0)
        largest_values = []
        while not node_queue.empty():
            node = node_queue.get()
            layer = layer_queue.get()
            if len(largest_values) <= layer:
                largest_values.append(node.val)
            elif largest_values[-1] < node.val:
                largest_values[-1] = node.val
            if node.left is not None:
                node_queue.put(node.left)
                layer_queue.put(layer + 1)
            if node.right is not None:
                node_queue.put(node.right)
                layer_queue.put(layer + 1)
        return largest_values

if __name__=="__main__":
    solution = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node2.left = node3
    node1.right = node4
    node4.right = node5
    node5.right = node6
    print(solution.largestValues(node1))

