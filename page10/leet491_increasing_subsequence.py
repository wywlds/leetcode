from typing import List

import copy
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        num_set = set()
        for num in nums:
            for i in range(len(ans)):
                an = ans[i]
                if num >= an[-1]:
                    ran = copy.deepcopy(an)
                    ran.append(num)
                    if str(ran) not in num_set:
                        ans.append(ran)
                        num_set.add(str(ran))
            if str([num]) not in num_set:
                ans.append([num])
                num_set.add(str([num]))
        ans_n = []
        for an in ans:
            if len(an) >= 2:
                ans_n.append(an)
        return ans_n

if __name__=="__main__":
    solution = Solution()
    l = [1,2,3,4,5,6]
    print(solution.findSubsequences(l))
    l = [1,2,3,1,4,5,6]
    print(solution.findSubsequences(l))
    l = [1,2,3,1,0,4,5,6,1]
    print(solution.findSubsequences(l))