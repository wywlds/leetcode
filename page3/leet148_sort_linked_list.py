class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next

        l.sort()
        head = cur = ListNode()
        for v in l:
            cur.next = ListNode(v)
            cur = cur.next
        return head.next
