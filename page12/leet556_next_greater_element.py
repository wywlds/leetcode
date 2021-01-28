class Solution:
    MAX_INT = 2**32 - 1
    def nextGreaterElement(self, n: int) -> int:
        stack = []
        while True:
            if n == 0:
                return -1
            i = n % 10
            n = n // 10
            if not stack or i >= stack[-1]:
                stack.append(i)
            else:
                first_digit = i
                break
        for i, digit in enumerate(stack):
            if digit > first_digit:
                tmp = digit
                stack[i] = first_digit
                break
        n = n * 10 + tmp
        while stack:
            digit = stack.pop(0)
            n = n * 10 + digit
        return n if n < self.MAX_INT else -1


if __name__=="__main__":
    solution = Solution()
    print(solution.nextGreaterElement(12))
    print(solution.nextGreaterElement(14321))