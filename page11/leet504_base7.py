class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        num_str = ""
        base = 7
        sign = ""
        if num < 0:
            sign = "-"
            num = -num
        residu = num

        while residu != 0:
            digit = (residu % base)//(base/7)
            num_str += str(int(digit))
            residu -= digit * (base // 7)
            base *= 7
        return sign+num_str[::-1]


if __name__=="__main__":
    solution = Solution()
    print(solution.convertToBase7(100))
    print(solution.convertToBase7(-7))

