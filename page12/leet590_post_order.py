from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        s = []
        result = []
        s.append(root)
        while s:
            node = s.pop()
            result.append(node.val)
            s.extend(node.children)
        return result[::-1]