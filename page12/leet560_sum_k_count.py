from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        dic = {}
        count = 0
        for num in nums:
            sum += num
            if sum in dic:
                count += dic[sum]
            if (sum + k) in dic:
                dic[sum+k] = dic[sum+k] + 1
            else:
                dic[sum+k] = 1
        return count