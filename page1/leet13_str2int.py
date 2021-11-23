class Solution:
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def romanToInt(self, s: str) -> int:
        i = 0
        ans = 0
        while i < len(s):
            for k, v in self.VALUE_SYMBOLS:
                if len(v) == 2 and i < len(s) - 1 and s[i] == v[0] and s[i + 1] == v[1]:
                    ans += k
                    i += 2
                    break
                elif len(v) == 1 and s[i] == v:
                    ans += k
                    i += 1
                    break
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))