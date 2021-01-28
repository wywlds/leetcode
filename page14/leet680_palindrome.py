class Solution:
    def exactPalindrome(self, s: str, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.exactPalindrome(s, l, r-1) or self.exactPalindrome(s, l + 1, r)
            l += 1
            r -= 1
        return True