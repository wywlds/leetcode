from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = min(bloomDay), max(bloomDay)
        if m * k > len(bloomDay):
            return -1

        def check(mid):
            ans, agg = 0, 0
            for bl in bloomDay:
                if bl <= mid:
                    agg += 1
                    if agg == k:
                        ans += 1
                        agg = 0
                else:
                    agg = 0
            return ans >= m

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
if __name__=="__main__":
    bloomDay = [7,7,7,7,12,7,7]
    m = 2
    k = 3
    solution = Solution()
    print(solution.minDays(bloomDay, m, k))