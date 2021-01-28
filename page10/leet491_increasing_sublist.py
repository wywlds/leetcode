from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        start, end = 0, 0
        for i, (cur_num, next_num) in enumerate(zip(nums[:-1], nums[1:])):
            if next_num >= cur_num:
                end += 1
            else:
                ans.extend(self.find_all(nums, start, end))
                start, end = i + 1, i + 1
        ans.extend(self.find_all(nums, start, end))
        return ans

    def find_all(self, nums, start, end):
        if end <= start:
            return []
        ans = []
        for i in range(start, end):
            for j in range(i+1, end+1):
                ans.append(nums[i : j + 1])
        return ans


if __name__=="__main__":
    solution = Solution()
    l = [1,2,3,4,5,6]
    print(solution.findSubsequences(l))
    l = [1,2,3,1,4,5,6]
    print(solution.findSubsequences(l))
    l = [1,2,3,1,0,4,5,6,1]
    print(solution.findSubsequences(l))