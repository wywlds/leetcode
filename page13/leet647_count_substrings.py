class Solution:
    def countSubstrings(self, s: str) -> int:
        LEN = len(s)
        ans = 0
        for i in range(2 * LEN - 1):
            left = i // 2
            right = (i + 1) // 2
            while left >= 0 and right <= LEN -1 and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans