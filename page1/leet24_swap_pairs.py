class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        before_head = ListNode(next=head)
        cur = head
        next = cur.next
        if next is not None:
            head = next

        while cur is not None or next is not None:
            cur.next = next.next
            next.next = cur
            before_head.next = next

            before_head = next
            cur = cur.next
            if cur is None:
                return head
            next = cur.next
        return head