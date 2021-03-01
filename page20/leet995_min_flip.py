from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flip_count = 0
        N = len(A)
        ans = 0
        for l in range(N):
            if l >= K and A[l - K] >= 2:
                flip_count -= 1
            if (A[l] & 1) == (flip_count & 1):
                if l + K > N:
                    return -1
                flip_count += 1
                A[l] += 2
                ans += 1
        return ans


if __name__=="__main__":
    A = [0,0,0,1,0,1,1,0]
    K = 3
    solution = Solution()
    print(solution.minKBitFlips(A, K))