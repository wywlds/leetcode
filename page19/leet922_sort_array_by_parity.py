from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 0
        N = len(A)
        ans = []
        while i < N and j < N:
            while i < N and A[i] % 2 == 1:
                i += 1
                continue
            if i != N:
                ans.append(A[i])
                i += 1
            while j < N and A[j] % 2 == 0:
                j += 1
                continue
            if j != N:
                ans.append(A[j])
                j += 1
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.sortArrayByParityII([4,2,5,7]))