from typing import List

import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstrs = []
        for num in nums:
            numstrs.append(str(num))
        def cmp(a, b):
            return int(b + a) - int(a + b)
        numstrs.sort(key=functools.cmp_to_key(cmp))
        if all([numstr == '0' for numstr in numstrs]):
            return "0"
        return "".join(numstrs)


if __name__=="__main__":
    solution = Solution()
    print(solution.largestNumber([3, 34]))