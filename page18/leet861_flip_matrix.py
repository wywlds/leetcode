from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        ans = m * (1 << (n - 1))
        for i in range(1, n):
            count_one = 0
            for j in range(m):
                if A[j][0] == 1 and A[j][i] == 1:
                    count_one += 1
                elif A[j][0] == 0 and A[j][i] == 0:
                    count_one += 1
            if count_one > m // 2:
                ans += count_one * (1 << (n - 1 - i))
            else:
                ans += (m - count_one) * (1 << (n - 1 -i))
        return ans


if __name__=="__main__":
    solution = Solution()
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(solution.matrixScore(A))