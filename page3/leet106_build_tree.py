from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root_val = postorder[-1]
        root_i = 0
        for i, val in enumerate(inorder):
            if val == root_val:
                root_i = i
        left_inorder = inorder[0:root_i]
        right_inorder = inorder[root_i+1:]
        left_postorder = postorder[0:root_i]
        right_postorder = postorder[root_i:len(postorder) - 1]
        left_tree = self.buildTree(left_inorder, left_postorder)
        right_tree = self.buildTree(right_inorder, right_postorder)
        root_node = TreeNode(root_val)
        root_node.left = left_tree
        root_node.right = right_tree
        return root_node

if __name__=="__main__":
    solution = Solution()
    tree = solution.buildTree([9,3,15,20,7], [9,15,7,20,3])
    pass