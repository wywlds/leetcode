from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        points.sort(key=lambda a : distance(a))
        return points[:K]


if __name__=="__main__":
    solution = Solution()
    print(solution.kClosest([[1,3],[-2,2]], 1))