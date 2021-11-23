class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        is_negative = x < 0
        x = abs(x)
        while x != 0:
            ans = ans * 10 + x % 10
            x //= 10
        if is_negative:
            ans = - ans
        if ans > 1 << 32 - 1 or ans < - 1 << 32:
            return 0
        return ans
