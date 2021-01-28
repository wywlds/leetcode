from typing import List

#N叉树前序遍历
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        s = []
        result = []
        s.append(root)
        while s:
            node = s.pop()
            result.append(node.val)
            s.extend(node.children[::-1])
        return result
