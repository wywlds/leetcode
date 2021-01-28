from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        downs = [[0] * COL for _ in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                if i == 0:
                    downs[i][j] = int(matrix[i][j])
                else:
                    downs[i][j] = 0 if matrix[i][j] == '0' else downs[i-1][j] + 1
        ans = 0
        for i in range(ROW):
            ans = max(self.max_column_area(downs[i]), ans)
        return ans

    def max_column_area(self, heights):
        if len(heights) == 0:
            return 0
        N = len(heights)
        rights = [N for _ in range(N)]
        lefts = [-1 for _ in range(N)]
        stk = []
        for i in range(N):
            while len(stk) > 0 and heights[stk[-1]] >= heights[i]:
                j = stk.pop()
                rights[j] = i
            lefts[i] = -1 if len(stk) == 0 else stk[-1]
            stk.append(i)
        ans = max([(rights[i] - lefts[i] - 1) * heights[i] for i in range(N)])
        return ans



if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    solution = Solution()
    print(solution.maximalRectangle(matrix))
