from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        weights = []
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            if i >= k:
                sum -= nums[i - k]
            if i >= k - 1:
                weights.append(sum)
        max_weights = []
        max_i = 0
        max_weight = -1
        for i, weight in enumerate(weights):
            if weight > max_weight:
                max_i = i
                max_weight = weight
            max_weights.append((max_i, max_weight))
        i_max_weights = []
        max_i = len(weights) - 1
        max_weight = weights[-1]
        for i in range(len(weights) - 1, -1, -1):
            weight = weights[i]
            if weight > max_weight:
                max_i = i
                max_weight = weight
            i_max_weights.insert(0, (max_i, max_weight))
        max_sum_weight = 0
        ans = None
        for i in range(k, len(weights) - k):
            left_i, left_weight = max_weights[i-k]
            right_i, right_weight = i_max_weights[i + k]
            if weights[i] + left_weight + right_weight > max_sum_weight:
                ans = [left_i, i, right_i]
                max_sum_weight = weights[i] + left_weight + right_weight
        return ans

if __name__=="__main__":
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    k = 2
    solution = Solution()
    print(solution.maxSumOfThreeSubarrays(nums, k))