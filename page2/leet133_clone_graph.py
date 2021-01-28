# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        nodes = {}
        def bfs(node):
            if not node:
                return
            q = deque()
            new_node = Node(node.val, [])
            q.appendleft(node)
            nodes[node] = new_node
            while q:
                cur_node = q.pop()
                for neighbor in cur_node.neighbors:
                    if neighbor not in nodes:
                        new_neighbor = Node(neighbor.val, [])
                        nodes[neighbor] = new_neighbor
                        q.appendleft(neighbor)
                    nodes[cur_node].neighbors.append(nodes[neighbor])
            return new_node
        

