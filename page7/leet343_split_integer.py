class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0
        num3 = n // 3
        residu3 = n % 3
        if residu3 == 0:
            return pow(3, num3)
        elif residu3 == 1:
            return pow(3, num3 - 1) * 4
        elif residu3 == 2:
            return pow(3, num3) * 2