from typing import List

import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        cur_l = []
        for i, num in enumerate(nums):
            l = bisect.bisect_left(cur_l, num)
            if l < len(cur_l) and abs(cur_l[l] - num) <= t:
                return True
            if l - 1 >= 0 and abs(cur_l[l - 1] - num) <= t:
                return True
            bisect.insort(cur_l, num)
            if len(cur_l) > k:
                ind = bisect.bisect_left(cur_l, nums[i - k])
                cur_l.pop(ind)
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate([0,1,2,3,1],3, 0))
