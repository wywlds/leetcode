class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N = len(t)
        mem = [0] * (N + 1)
        for ch in s:
            for i in range(N - 1, -1, -1):
                if ch == t[i]:
                    if i == 0:
                        mem[i] += 1
                    else:
                        mem[i] = mem[i - 1] + mem[i]
            continue
        return mem[N - 1]

if __name__=="__main__":
    s = "babgbag"
    t = "bag"
    # s = "rabbbit"
    # t = "rabbit"
    solution = Solution()
    print(solution.numDistinct(s, t))