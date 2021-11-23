from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        hs = []
        w = 0
        for i, h in enumerate(height):
            while len(hs) != 0 and hs[-1][1] <= h:
                _, last_h = hs.pop()
                if len(hs) != 0:
                    delta_h = min(h, hs[-1][1]) - last_h
                    l = i - hs[-1][0]  - 1
                    w += l * delta_h
            hs.append((i, h))
        return w

if __name__=="__main__":
    solution = Solution()
    print(solution.trap([2, 1, 0, 3]))
