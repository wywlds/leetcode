from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        MAX = len(obstacles) + 100
        mem = [MAX] * 3
        mem[1] = 0
        for obstacle in obstacles:
            if obstacle != 0:
                mem[obstacle - 1] = MAX
            min_value = min(mem)
            for i in range(3):
                if i != obstacle - 1:
                    mem[i] = min(mem[i], min_value + 1)
        return min(mem)

if __name__=="__main__":
    obstacles = [0,1,2,3,0]
    solution = Solution()
    print(solution.minSideJumps(obstacles))