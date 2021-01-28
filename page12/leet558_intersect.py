# Definition for a QuadTree node.
### 这个题先写了广度遍历，又从广度遍历中回复到四叉树，最后又根据深度遍历回归到结果，真是啥都做过了，
### 其实一个简单的迭代，深度遍历就可以了
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
from collections import deque
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        queue1 = deque([quadTree1])
        queue2 = deque([quadTree2])
        result = []
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            result.append(self.get_value(node1, node2))
            if node1.isLeaf and node2.isLeaf:
                continue
            queue1.extend(self.get_children(node1))
            queue2.extend(self.get_children(node2))

        first_node = result.pop(0)
        first_node = Node(first_node[1], first_node[0], None, None, None, None)
        parent_nodes = deque([first_node])
        i = 4
        parent_node = None
        for isLeaf, val in result:
            node = Node(val, isLeaf, None, None, None, None)
            if i == 4:
                parent_node = parent_nodes.popleft()
                i = 0
            self.add_node_by_index(parent_node, node, i)
            i += 1
            if not isLeaf:
                parent_nodes.append(node)
        return self.dfs(first_node)


    def get_value(self, node1, node2):
        return [node1.isLeaf and node2.isLeaf, node1.val or node2.val]

    def get_children(self, node1):
        if node1.isLeaf:
            return [Node(node1.val, 1, None, None, None, None) for _ in range(4)]
        else:
            return [node1.topLeft, node1.topRight, node1.bottomLeft, node1.bottomRight]

    def add_node_by_index(self, parent_node, node, i):
        if i == 0:
            parent_node.topLeft = node
        elif i == 1:
            parent_node.topRight = node
        elif i == 2:
            parent_node.bottomLeft = node
        else:
            parent_node.bottomRight = node

    def dfs(self, first_node):
        if first_node.isLeaf:
            return first_node
        children = [first_node.topLeft, first_node.topRight, first_node.bottomLeft, first_node.bottomRight]
        [self.dfs(child) for child in children]
        all_leaf = all([child.isLeaf == 1 for child in children])
        all_one = all([child.val == 1 for child in children])
        all_zero = all([child.val == 0 for child in children])
        if all_leaf and (all_one or all_zero):
            first_node.isLeaf = 1
            first_node.val = 1 if all_one else 0
            first_node.topLeft = None
            first_node.topRight = None
            first_node.bottomRight = None
            first_node.bottomLeft = None
        if not all_one:
            first_node.val = 0
        return first_node