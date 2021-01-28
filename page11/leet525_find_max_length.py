from typing import List

# 这道题目挺有意思的，用前缀和来理解，同一个前缀和说明两个之间的0和1的数目一致
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt_dict = {}
        agg_cnt = 0
        max_len = 0
        for i, num in enumerate(nums):
            if num == 1:
                agg_cnt += 1
            if num == 0:
                agg_cnt -= 1
            if agg_cnt in cnt_dict:
                start_index = cnt_dict[agg_cnt]
                max_len = max(max_len, i - start_index + 1)
            else:
                cnt_dict[agg_cnt] = i
        return max_len

