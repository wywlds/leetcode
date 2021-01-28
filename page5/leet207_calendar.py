from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacent = [[] for i in range(numCourses)]
        flags = [0] * numCourses
        def dfs(i):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in adjacent[i]:
                if not dfs(j):
                    return False
            flags[i] = 1
            return True
        for i, j in prerequisites:
            adjacent[i].append(j)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
