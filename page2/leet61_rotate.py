from page1.leet19_remove_nth import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 1
        cur = head
        while cur.next is not None:
            cur = cur.next
            n += 1
        end = cur
        k = (n - k) % n
        if k == 0:
            return head
        n = 1
        cur = head
        while n < k:
            cur = cur.next
            n += 1
        cur_next =cur.next
        end.next = head
        cur.next = None
        return cur_next
