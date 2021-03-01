from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        group_i = 0
        GLEN = len(groups)
        NLEN = len(nums)
        def matched(i, group_i):
            target = groups[group_i]
            LEN = len(target)
            for cur in range(LEN):
                if i + cur < NLEN and nums[i + cur] == target[cur]:
                    continue
                else:
                    return False
            return True

        i = 0
        while i < len(nums):
            if matched(i, group_i):
                i += len(groups[group_i])
                group_i += 1
                if group_i == GLEN:
                    return True
            else:
                i += 1
        return False

if __name__=="__main__":
    groups = [[10,-2],[1,2,3,4]]
    nums =[1,2,3,4,10,-2]
    solution = Solution()
    print(solution.canChoose(groups, nums))