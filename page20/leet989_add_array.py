from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i = len(A) - 1
        res = 0
        ans = []
        while K != 0 or i >= 0 or res != 0:
            right_res, K = K % 10, K//10
            left_res = A[i] if i >= 0 else 0
            i = i - 1 if i>= 0 else i
            cur, res = (right_res + left_res + res) % 10, (right_res + left_res + res) // 10
            ans.append(cur)
        return ans[::-1]


if __name__=="__main__":
    solution = Solution()
    A, K = [4,0, 0], 656
    print(solution.addToArrayForm(A, K))