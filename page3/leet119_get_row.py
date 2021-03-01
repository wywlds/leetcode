from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex + 1):
            if i == 0:
                ans.append(1)
            else:
                ans.append(ans[-1] * (rowIndex - i + 1) // i)
        return ans

if __name__=="__main__":
    solution = Solution()
    for i in range(0, 10):
        print(solution.getRow(i))