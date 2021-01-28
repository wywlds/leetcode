class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_header = ListNode()
        even_header = ListNode()
        odd_tail, even_tail = odd_header, even_header
        cur = head
        while cur is not None:
            odd_tail.next = cur
            even_tail.next = cur.next if cur is not None else None
            odd_tail = odd_tail.next
            even_tail = even_tail.next
            cur = even_tail.next if even_tail is not None else None
        odd_tail.next = even_header.next
        return odd_header.next

def link(nodes, n):
    if n == 0:
        return None
    for pnode, nnode in zip(nodes[:n-1], nodes[1:]):
        pnode.next = nnode
    return nodes[0]

def _print(node):
    ans = []
    while node is not None:
        ans.append(str(node.val))
        node = node.next
    print("%s" % ans)


if __name__=="__main__":
    solution = Solution()
    nodes = [ListNode(n) for n in range(5)]
    for n in range(len(nodes) + 1):
        head = link(nodes, n)
        solution.oddEvenList(head)
        _print(head)