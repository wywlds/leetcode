from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1 or N == 2:
            return True
        dp = [[nums[i], nums[i + 1]] if nums[i + 1] > nums[i] else [nums[i + 1], nums[i]] for i in range(N - 1)]
        for rnd in range(2, N):
            p = rnd % 2
            for i in range(N - rnd):
                d_start = [0, 0]
                d_start[p] = nums[i]
                d_end = [0, 0]
                d_end[p] = nums[i + rnd]
                start = [dp[i][0] + d_end[0], dp[i][1] + d_end[1]]
                end = [dp[i + 1][0] + d_start[0], dp[i + 1][1] + d_start[1]]
                if start[p] > end[p]:
                    dp[i] = start
                else:
                    dp[i] = end
        p = (N - 1) % 2
        if dp[0][p] >= dp[0][(p + 1) % 2]:
            return True
        else:
            return False


if __name__=="__main__":
    solution = Solution()
    print(solution.PredictTheWinner([1,5,2,4,6]))
    print(solution.PredictTheWinner([1, 5, 233, 7]))
