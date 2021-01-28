from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candys[i] = candys[i-1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candys[i] = max(candys[i], candys[i + 1] + 1)
        return sum(candys)


if __name__=="__main__":
    solution = Solution()
    solution.candy([1, 2, 2, 3])
    solution.candy([1, 2, 3, 4, 5, 3, 4, 2, 1])