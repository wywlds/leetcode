class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.sorted_list_to_bst(head, None)

    def sorted_list_to_bst(self, head, end):
        slow = head
        fast = head
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = fast.next
        head = TreeNode(slow.val)
        head.left = self.sorted_list_to_bst(head, slow)
        head.right = self.sorted_list_to_bst(slow.next, end)
        return head