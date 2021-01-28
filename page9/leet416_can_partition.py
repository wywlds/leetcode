from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if len(nums) < 2:
            return False

        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2

        sums = [0]
        sum_set = set()
        for num in nums:
            len_sums = len(sums)
            for sum_i in sums[0:len_sums]:
                sum_n = sum_i + num
                if sum_n not in sum_set:
                    sums.append(sum_n)
                    sum_set.add(sum_n)
        if target in sum_set:
            return True
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.canPartition([1,5,11,5]))