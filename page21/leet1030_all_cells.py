from typing import List
import collections


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        q = collections.deque()
        visited = set()
        q.append((r0, c0))
        visited.add((r0, c0))
        ans = []
        while len(q) != 0:
            r, c = q.popleft()
            ans.append([r, c])
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = r + dx, c + dy
                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        return ans


if __name__=="__main__":
    R = 2
    C = 2
    r0 = 0
    c0 = 1
    solution = Solution()
    print(solution.allCellsDistOrder(R, C, r0, c0))