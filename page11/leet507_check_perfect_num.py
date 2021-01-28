import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum = 1
        root = math.sqrt(num)
        for i in range(2, math.floor(root) + 1):
            res = num / i
            if math.floor(res) == math.ceil(res):
                sum += i
                if int(res) != i:
                    sum += int(res)
            if sum > num:
                return False

        if sum == num:
            return True
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.checkPerfectNumber(28))
    print(solution.checkPerfectNumber(1))
    print(solution.checkPerfectNumber(0))
    print(solution.checkPerfectNumber(2))
    print(solution.checkPerfectNumber(6))