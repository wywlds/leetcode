class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        b_node = ListNode()
        b_node.next = head

        cur_node = b_node
        i = 1
        while i != left:
            cur_node = cur_node.next
            i += 1

        len = right - left + 1
        if len == 1:
            return head

        start_node = cur_node.next
        next_node = start_node.next

        j = 0
        while j < len - 1:
            tmp_node = next_node.next
            next_node.next = start_node
            start_node = next_node
            next_node = tmp_node
            j += 1
        cur_node.next.next = next_node
        cur_node.next = start_node
        return b_node.next


if __name__=="__main__":
    listNode1 = ListNode(1)
    listNode2 = ListNode(2)
    listNode3 = ListNode(3)
    listNode4 = ListNode(4)
    listNode5 = ListNode(5)
    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    listNode4.next = listNode5
    solution = Solution()
    solution.reverseBetween(listNode1, 1, 5)

    node = listNode5
    while node != None:
        print(node.val)
        node = node.next
