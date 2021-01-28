class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = list(str(N))
        i = 0
        while True:
            if i == len(digits) - 1 or digits[i + 1] < digits[i]:
                break
            i += 1
        if i < len(digits) - 1:
            while True:
                digits[i] = str(int(digits[i]) - 1)
                i -= 1
                if i < 0 or digits[i + 1] >= digits[i]:
                    break
            for l in range(i + 2, len(digits)):
                digits[l] = '9'
        return int("".join(digits))

if __name__=="__main__":
    solution = Solution()
    print(solution.monotoneIncreasingDigits("123"))
    print(solution.monotoneIncreasingDigits("122"))
    print(solution.monotoneIncreasingDigits(121))
    print(solution.monotoneIncreasingDigits("1000000000"))

