from typing import List
import bisect


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sorted_nums = sorted(nums)
        LEN = len(nums)

        medals = []
        for num in nums:
            rank = LEN - bisect.bisect_left(sorted_nums, num)
            if rank == 1:
                medals.append("Gold Medal")
            elif rank == 2:
                medals.append("Silver Medal")
            elif rank == 3:
                medals.append("Bronze Medal")
            else:
                medals.append(str(rank))
        return medals

if __name__=="__main__":
    solution = Solution()
    print(solution.findRelativeRanks([5, 4, 3, 2, 1]))