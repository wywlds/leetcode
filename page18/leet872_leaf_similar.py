class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs1 = []
        leafs2 = []
        def visit(node, leafs):
            if node.left is None and node.right is None:
                leafs.append(node.val)
            else:
                if node.left is not None:
                    visit(node.left, leafs)
                if node.right is not None:
                    visit(node.right, leafs)
        visit(root1, leafs1)
        visit(root2, leafs2)
        return leafs1 == leafs2