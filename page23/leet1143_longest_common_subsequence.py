class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = [[0] * len(text2) for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        mem[i][j] = 1
                    else:
                        mem[i][j] = max(mem[i-1][j], mem[i][j-1], mem[i-1][j-1] + 1)
                else:
                    if i == 0:
                        mem[i][j] = mem[i][j-1]
                    elif j == 0:
                        mem[i][j] = mem[i-1][j]
                    else:
                        mem[i][j] = max(mem[i-1][j], mem[i][j-1])
        return mem[len(text1) - 1][len(text2) - 1]


if __name__=="__main__":
    solution = Solution()
    print(solution.longestCommonSubsequence("abcd", "aadbc"))