from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num = float('inf')
        max_num = float('-inf')
        for num in nums:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
        bar_width = max(1, (max_num - min_num) // (len(nums) - 1))
        bucket_size = (max_num - min_num) // bar_width + 1
        bucket_max = [-1] * (bucket_size )
        bucket_min = [-1] * (bucket_size)
        for num in nums:
            bucket_index = (num - min_num) // bar_width
            bucket_max[bucket_index] = max(bucket_max[bucket_index], num)
            bucket_min[bucket_index] = min(bucket_min[bucket_index], num) if bucket_min[bucket_index] != -1 else num

        max_delta = 0
        last_max = bucket_max[0]
        for i in range(1, bucket_size):
            if bucket_min[i] != -1 and last_max != -1:
                max_delta = max(max_delta, bucket_min[i] - last_max)
            if bucket_max[i] != -1:
                last_max = bucket_max[i]

        return max_delta


if __name__=="__main__":
    solution = Solution()
    print(solution.maximumGap([1000,1]))