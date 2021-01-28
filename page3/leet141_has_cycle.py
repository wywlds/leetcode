class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head.next
        fast = head.next.next
        while slow != fast and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is None or fast.next is None:
            return False
        else:
            return True
