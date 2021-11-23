from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        LEN = len(nums)
        def dfs(base, i, pre):
            if i >= LEN:
                return
            dfs(base, i + 1, 0)
            if not (pre == 0 and i != 0 and nums[i] == nums[i - 1]):
                base.append(nums[i])
                ans.append(base[:])
                dfs(base, i + 1, 1)
                base.pop()
        ans.append([])
        dfs([], 0, 0)
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.subsetsWithDup([1,2,2,2]))