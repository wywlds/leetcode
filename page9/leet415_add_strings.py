class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            return self.addString(num2, num1)
        i_num1 = num1[::-1]
        i_num2 = num2[::-1]

        ans = ""
        tmp = 0
        for i, ni1 in enumerate(i_num1):
            ni2 = i_num2[i] if i < len(i_num2) else '0'
            ni1, ni2 = ord(ni1) - ord('0'), ord(ni2) - ord('0')
            added = ni1 + ni2 + tmp
            cur = added % 10
            tmp = added // 10
            ans += str(cur)
        if tmp != 0:
            ans += str(tmp)
        return ans[::-1]


if __name__=="__main__":
    solution = Solution()
    print(solution.addStrings("123", "12"))