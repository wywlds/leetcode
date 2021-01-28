from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                dist.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        dist.sort()

        parents = [-1] * len(points)
        NUM = len(points) - 1
        def find(x):
            if parents[x] < 0:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x == parent_y:
                return False
            parents[parent_x] = parent_y
            return True
        num = 0
        ans = 0
        for d, x, y in dist:
            if union(x, y):
                num += 1
                ans += d
                if num == NUM:
                    break
        return ans


if __name__=="__main__":
    ps = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()
    print(solution.minCostConnectPoints(ps))