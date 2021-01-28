import collections

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = collections.deque()
        queue.append((root, 1))
        max_depth = 0
        while queue:
            node, depth = queue.pop()
            max_depth = max(max_depth, depth)
            queue.extendleft([(child, depth + 1) for child in node.children])
        return max_depth
