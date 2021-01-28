class Solution:
    def checkValidString(self, s: str) -> bool:
        max_n = 0
        min_n = 0
        for ch in s:
            if ch == "(":
                max_n += 1
                min_n -= 1
            elif ch == "*":
                max_n += 1
                min_n -= 1
            else:
                max_n -= 1
                min_n -= 1
            if max_n < 0:
                return False
        return min_n <= 0