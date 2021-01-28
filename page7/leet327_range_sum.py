from itertools import accumulate
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        acc = [0] + list(accumulate(nums))
        return self.counter_recursive(acc, lower, upper, 0, len(acc) - 1)

    def counter_recursive(self, acc, lower, upper, l, r):
        if l == r:
            return 0
        else:
            mid = (l + r) // 2
            l_c = self.counter_recursive(acc, lower, upper, l, mid)
            r_c = self.counter_recursive(acc, lower, upper, mid + 1, r)
            ret = l_c + r_c

            i, r_u, r_l = l, mid + 1, mid + 1
            while i <= mid:
                while r_u <= r and acc[r_u] <= acc[i] + upper:
                    r_u += 1
                while r_l <= r and acc[r_l] < acc[i] + lower:
                    r_l += 1
                ret += (r_u - r_l)
                i += 1

            left = acc[l:mid+1] + [float('inf')]
            right = acc[mid+1:r+1] + [float('inf')]
            p = l
            l_p, r_p = 0, 0
            while p <= r:
                if left[l_p] < right[r_p]:
                    acc[p] = left[l_p]
                    l_p += 1
                else:
                    acc[p] = right[r_p]
                    r_p += 1
                p += 1
            return ret

if __name__=="__main__":
    solution = Solution()
    print(solution.countRangeSum([-2,5,-1], -2, 2))