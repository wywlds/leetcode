import re
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        num_re = re.compile("^[\+\-]?\d+")
        nums = num_re.findall(str)
        num = int(*nums)
        return max(min(num, 2**31-1), -2**31)

if __name__=="__main__":
    solution = Solution()
    print(solution.myAtoi("42"))