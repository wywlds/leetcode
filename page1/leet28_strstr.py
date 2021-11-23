class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        for matcher in re.finditer(needle, haystack):
            return matcher.span()[0]
        return -1
