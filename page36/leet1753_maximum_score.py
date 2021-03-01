class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l = [a, b, c]
        l.sort()
        ans = a
        if a >= abs(b - c):
            ans += (b + c - ans) // 2
        else:
            ans += min(b, c)
        return ans