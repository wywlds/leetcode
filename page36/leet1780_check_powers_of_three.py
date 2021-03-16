class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            cur = n % 3
            if cur == 2:
                return False
            n = n // 3
        return True