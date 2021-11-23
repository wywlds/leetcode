class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        mem = [0] * len(s)
        mem[0] = 1
        mem[1] = 1 if 10 <= int(s[0:2]) <= 26 else 0
        if s[1] != '0':
            mem[1] = mem[1] + mem[0]
        for i in range(2, len(s)):
            ch = s[i]
            last2 = s[i-1: i+1]
            if ch != '0':
                mem[i] = mem[i-1]
            if 10 <= int(last2) <= 26:
                mem[i] += mem[i - 2]
        return mem[-1]


if __name__=="__main__":
    solution = Solution()
    print(solution.numDecodings("112002"))
