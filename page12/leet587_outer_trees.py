from typing import List

import math
import functools
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 3:
            return points
        minx, miny = 101, 101
        for x, y in points:
            if y < miny:
                minx, miny = x, y
            elif y == miny:
                minx = min(x, minx)
        others = [[x, y] for x, y in points if x != minx or y != miny]

        def cmp(x, y):
            orient = Solution.orient([minx, miny], y, x)
            if orient > 0:
                return 1
            elif orient < 0:
                return -1
            else:
                return Solution.distance([minx, miny],x) - Solution.distance([minx, miny], y)

        others.sort(key=functools.cmp_to_key(cmp))
        others.reverse()
        len_equal = 0
        for i, point in enumerate(others):
            if self.orient([minx, miny], others[0], point) == 0:
                len_equal = i
            else:
                break
        new_others = others[0:len_equal+1][::-1]
        new_others.extend(others[len_equal+1:])
        others = new_others[::-1]
        s = []
        s.extend([[minx, miny], others[0]])
        for i in range(1, len(others)):
            new_p = others[i]
            while True:
                if len(s) == 1:
                    s.append(new_p)
                    break
                top_p = s[-1]
                last_p = s[-2]
                if self.orient(last_p, top_p, new_p) < 0:
                    s.pop()
                else:
                    s.append(new_p)
                    break
        return s

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    @staticmethod
    def orient(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1])*(p3[0] - p2[0])

if __name__=="__main__":
    solution = Solution()
    print(solution.orient([4,2], [3,3], [2,4]))
    print(solution.outerTrees([[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[3,3]]))