class Solution:
    def countArrangement(self, N: int) -> int:
        self.visited = set()
        self.all = set(list(range(1, N+1)))
        self.num = 0
        self.N = N
        def dfs(i):
            if i == self.N + 1:
                self.num += 1
                return
            candidates = self.all - self.visited
            for candidate in candidates:
                if candidate % i == 0 or i % candidate == 0:
                    self.visited.add(candidate)
                    dfs(i+1)
                    self.visited.remove(candidate)
        dfs(1)
        return self.num


if __name__=="__main__":
    solution = Solution()
    print(solution.countArrangement(15))