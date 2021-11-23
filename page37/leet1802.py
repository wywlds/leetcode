class Solution:
    def getMinimumSum(self, n, index, m):
        m = m - 1
        base = 0
        if m <= index:
            base += m * (m + 1) // 2
        else:
            base += (index + 1) * (m + m - index) // 2
        left_index = n - 1 - index
        if m <= left_index:
            base += m * (m + 1) // 2
        else:
            base += (left_index + 1) * (2 * m - left_index) // 2
        base += n
        return base - m

    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        l, r = 1, maxSum
        while l <= r:
            m = (l + r) // 2
            if self.getMinimumSum(n, index, m) > maxSum:
                r = m - 1
            else:
                l = m + 1
        return r

if __name__=="__main__":
    n = 6
    index = 1
    maxSum = 10
    solution = Solution()
    print(solution.getMinimumSum(n, index, 3))
    print(solution.maxValue(n, index, maxSum))