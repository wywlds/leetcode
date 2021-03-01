from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            if i != num - 1:
                j, tmp_num = i, num
                while True:
                    if tmp_num - 1 != j and nums[tmp_num - 1] != tmp_num:
                        tmp = nums[tmp_num - 1]
                        nums[tmp_num - 1] = tmp_num
                        tmp_num = tmp
                    else:
                        break
                nums[i] = tmp_num
        ans = []
        for i, num in enumerate(nums):
            if i != num - 1:
                ans.append(i + 1)
        return ans

if __name__=="__main__":
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    print(solution.findDisappearedNumbers(nums))
