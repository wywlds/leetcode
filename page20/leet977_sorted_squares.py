from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        spliter = len(A)
        for i in range(len(A)):
            if A[i] > 0:
                spliter = i
                break
        if spliter == len(A):
            return [num ** 2 for num in A[::-1]]
        elif spliter == 0:
            return [num ** 2 for num in A]
        else:
            i, j = spliter, spliter + 1
            N = len(A)
            A.append(float('inf'))
            A.insert(0, float('-inf'))
            ans = []
            for _ in range(N):
                if A[j] < -A[i]:
                    ans.append(A[j] ** 2)
                    j += 1
                else:
                    ans.append(A[i] ** 2)
                    i -= 1
            return ans

if __name__=="__main__":
    solution = Solution()
    solution.sortedSquares([-7,-3,2,3,11])