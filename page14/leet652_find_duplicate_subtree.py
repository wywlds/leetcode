from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.counter = {}
        self.result = []
        self.postOrder(root)
        return self.result

    def postOrder(self, node):
        if node == None:
            return {}
        left_desc = self.postOrder(node.left)
        right_desc = self.postOrder(node.right)
        desc = "(%d : %s %s)" % (node.val, left_desc, right_desc)
        if desc not in self.counter:
            self.counter[desc] = 1
        elif self.counter[desc] == 1:
            self.counter[desc] += 1
            self.result.append(node)
        return desc