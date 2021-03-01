from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start, end = 0, 0
        N = len(A)
        cnt_flipped = 0
        while end < N and (cnt_flipped < K or A[end] == 1):
            if A[end] == 0:
                A[end] = 2
                cnt_flipped += 1
            end += 1
        ans = end - start
        while end < N:
            if A[end] == 0:
                while start< end and A[start] != 2:
                    start += 1
                start += 1
                A[end] = 2
            ans = max(end-start + 1, ans)
            end += 1
        return ans


if __name__=="__main__":
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K = 0
    solution = Solution()
    print(solution.longestOnes(A, K))