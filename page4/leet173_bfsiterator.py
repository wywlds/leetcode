from page11.leet501_find_mode import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.s = []
        self.push_stack(root)

    def push_stack(self, node):
        while node is not None:
            self.s.append(node)

    def next(self) -> int:
        cur = self.s.pop()
        self.push_stack(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return len(self.s) != 0