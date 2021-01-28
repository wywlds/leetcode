class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tail = head
        for _ in range(n - 1):
            tail = tail.next
        helper = ListNode(next=head)
        while tail.next != None:
            helper = helper.next
            tail = tail.next

        deleted = helper.next
        helper.next = helper.next.next
        if deleted == head:
            return helper.next
        else:
            return head