from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(list(str)))
            ans_dict[sorted_str].append(str)
        return list(ans_dict.values())


if __name__=="__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))