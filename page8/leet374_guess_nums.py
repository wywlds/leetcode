def guess(num):
    if num < 10:
        return 1
    elif num > 10:
        return -1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            gu = guess(m)
            if gu == 0:
                return m
            elif gu > 0:
                l = m + 1
            else:
                r = m - 1
        return -1

if __name__=="__main__":
    solution = Solution()
    print(solution.guessNumber(12))