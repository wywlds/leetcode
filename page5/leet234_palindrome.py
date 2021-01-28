class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fake = ListNode(0)
        fake.next = head
        fast, slow = fake, fake

        values = []
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            values.append(slow.val)

        if fast is None:
            values.pop()
        while slow.next is not None:
            slow = slow.next
            if values[-1] == slow.val:
                values.pop()
            else:
                return False
        return len(values) == 0


if __name__=="__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l1.next = l2
    l2.next = l3
    solution = Solution()
    solution.isPalindrome(l1)