class Solution:
    num_trees = {0:1, 1:1, 2:2}
    def numTrees(self, n: int) -> int:
        if n in self.num_trees:
            return self.num_trees[n]
        num_trees = 0
        for i in range(n):
            left_count = self.numTrees(i)
            right_count = self.numTrees(n - 1 - i)
            num_trees += left_count * right_count
        self.num_trees[n] = num_trees
        return num_trees


if __name__=="__main__":
    solution = Solution()
    print(solution.numTrees(3))