class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        columns = set()
        diag1 = set()
        diag2 = set()

        def dfs(N):
            nonlocal ans
            if N == n:
                ans += 1
                return
            for i in range(n):
                if i in columns or (i + N) in diag1 or (i - N) in diag2:
                    continue
                columns.add(i)
                diag1.add(i+N)
                diag2.add(i-N)
                dfs(N + 1)
                columns.remove(i)
                diag1.remove(i+N)
                diag2.remove(i-N)
        dfs(0)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.totalNQueens(8))