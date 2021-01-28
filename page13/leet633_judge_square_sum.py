import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max = int(math.sqrt(c))
        left_set = set()
        for i in range(1, max + 1):
            square = i ** 2
            if square in left_set:
                return True
            left = c - square
            left_set.add(left)
        return False


if __name__=="__main__":
    solution = Solution()
    solution.judgeSquareSum(5)