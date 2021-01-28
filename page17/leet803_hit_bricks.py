from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        parents = {}
        def find(i, j):
            if isinstance(parents[(i, j)], int):
                return (i, j)
            parents[(i, j)] = find(*parents[(i, j)])
            return parents[(i, j)]

        def union(i1, j1, i2, j2):
            if (i1, j1) not in parents or (i2, j2) not in parents:
                return
            root1 = find(i1, j1)
            root2 = find(i2, j2)
            if root1 == root2:
                return
            elif root1 < root2:
                count2 = parents[root2]
                parents[root2] = root1
                parents[root1] += count2
            else:
                count1 = parents[root1]
                parents[root1] = root2
                parents[root2] += count1

        parents[(-1, -1)] = 0
        ans = [-1] * len(hits)
        ANSLEN = len(ans)
        for r, (i, j) in enumerate(hits):
            if grid[i][j] == 0:
                ans[r] = 0
            else:
                grid[i][j] = 0

        for i, l in enumerate(grid[0]):
            if l == 1:
                parents[(0, i)] = 1
                union(0, i, -1, -1)

        for i in range(1, M):
            for j in range(N):
                if grid[i][j] == 1:
                    parents[(i, j)] = 1
                    union(i, j, i-1, j)
                    union(i, j, i, j -1)

        for i, (hit_i, hit_j) in enumerate(hits[::-1]):
            if ans[ANSLEN - 1 - i] == 0:
                continue
            base_num = parents[(-1, -1)]
            parents[(hit_i, hit_j)] = 1
            if hit_i == 0:
                union(hit_i, hit_j, -1, -1)
            union(hit_i, hit_j, hit_i - 1, hit_j)
            union(hit_i, hit_j, hit_i + 1, hit_j)
            union(hit_i, hit_j, hit_i, hit_j - 1)
            union(hit_i, hit_j, hit_i, hit_j + 1)
            ans[ANSLEN - 1 - i] = max(0, parents[(-1, -1)] - base_num - 1)
        return ans

if __name__=="__main__":
    grid = [[1],[1],[1],[1],[1]]
    hits = [[3,0],[4,0],[1,0],[2,0],[0,0]]
    solution = Solution()
    print(solution.hitBricks(grid, hits))