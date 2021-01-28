class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo = 1
        hi = m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if (not self.enough(m, n, mi, k)):
                lo = mi + 1
            else:
                hi = mi
        return lo

    def enough(self, m, n, mi, k):
        count = 0
        for i in range(m):
            count += min(n, mi // i)
        return count >= k