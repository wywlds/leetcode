from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        LEN = len(nums)
        counter = Counter(nums)
        ans = []
        def dfs(base_list):
            if len(base_list) == LEN:
                ans.append(base_list[:])
                return
            items = counter.most_common()
            for item, count in items:
                if count == 0:
                    continue
                base_list.append(item)
                counter[item] = count - 1
                dfs(base_list)
                base_list.pop()
                counter[item] = count
        dfs([])
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.permuteUnique([1,1,2]))