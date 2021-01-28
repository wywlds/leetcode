from typing import List

import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        ans = []
        cur_candi = candidates[0]
        candidates_new = candidates[1:]
        residu = target
        base = []
        while residu > 0:
            sub_ans = self.combinationSum(candidates_new, residu)
            if len(sub_ans) > 0:
                new_ans = []
                for sub in sub_ans:
                    base_c = copy.deepcopy(base)
                    base_c.extend(sub)
                    new_ans.append(base_c)
                ans.extend(new_ans)
            base.append(cur_candi)
            residu -= cur_candi
        if residu == 0:
            ans.append(base)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.combinationSum([2,3,5], 9))