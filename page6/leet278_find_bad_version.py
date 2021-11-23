def isBadVersion(version):
    if version >= 10:
        return True
    else:
        return False
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return r + 1


if __name__=="__main__":
    solution = Solution()
    print(solution.firstBadVersion(12))