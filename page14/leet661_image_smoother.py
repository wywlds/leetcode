from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        deltas = [(-1,-1), (-1, 0), (0,-1), (0,1), (1,0), (1,1), (1,-1), (-1,1), (0,0)]
        A, B = len(M), len(M[0])
        result = [[0] * B for _ in range(A)]
        for i in range(A):
            for j in range(B):
                sum = 0
                count = 0
                for dx, dy in deltas:
                    x, y = i + dx, j + dy
                    if 0<=x<A and 0<=y<B:
                        sum += M[x][y]
                        count += 1
                result[i][j] = int(sum/count)
        return result


if __name__=="__main__":
    solution = Solution()
    print(solution.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))