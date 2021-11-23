from page1.leet19_remove_nth import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        b = ListNode()
        last = b
        cur_node = head
        while cur_node is not None:
            if (cur_node.next is not None and cur_node.next.val != cur_node.val) or cur_node.next is None:
                last.next = cur_node
                last = cur_node
            cur_node = cur_node.next
        last.next = None
        return b.next