from typing import List

from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter = Counter()
        ans = 0
        l, r = 0, 0
        while r < len(A):
            counter[A[r]] += 1
            while len(counter) >= K and l <= r:
                if len(counter) == K:
                    tr = r
                    while tr < len(A) and counter[A[tr]] > 0:
                        ans += 1
                        tr += 1
                if counter[A[l]] == 1:
                    counter.pop(A[l])
                else:
                    counter[A[l]] -= 1
                l += 1
            r += 1
        return ans

if __name__=="__main__":
    A = [1,2,1,2,3]
    K = 2
    solution = Solution()
    print(solution.subarraysWithKDistinct(A, K))

    A = [1,2,1,3,4]
    K = 3
    print(solution.subarraysWithKDistinct(A, K))
