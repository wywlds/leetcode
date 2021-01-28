import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        node_queue = queue.Queue()
        layer_queue = queue.Queue()
        last_layer = 0
        last_val = root.val
        node_queue.put(root)
        layer_queue.put(last_layer)
        while not node_queue.empty():
            cur_node = node_queue.get()
            cur_layer = layer_queue.get()
            if cur_layer > last_layer:
                last_layer = cur_layer
                last_val = cur_node.val
            if cur_node.left is not None:
                node_queue.put(cur_node.left)
                layer_queue.put(cur_layer + 1)
            if cur_node.right is not None:
                node_queue.put(cur_node.right)
                layer_queue.put(cur_layer+1)
        return last_val

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
    print(solution.findBottomLeftValue(node1))