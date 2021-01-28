class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [0] * n
        mem[0] = 1
        for _ in range(m):
            for j in range(1, n):
                mem[j] = mem[j] + mem[j - 1]
        return mem[-1]


if __name__=="__main__":
    solution = Solution()
    print(solution.uniquePaths(7, 3))