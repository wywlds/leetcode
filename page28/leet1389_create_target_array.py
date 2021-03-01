from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for num, i in zip(nums, index):
            ans.insert(i, num)
        return ans

if __name__=="__main__":
    nums = [1,2,3,4,0]
    index = [0,1,2,3,0]
    solution = Solution()
    print(solution.createTargetArray(nums, index))