class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = small = ListNode(0)
        dummy2 = large = ListNode(0)
        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        if dummy1.next is None:
            return dummy2.next
        small.next = dummy2.next
        large.next = None
        return dummy1.next