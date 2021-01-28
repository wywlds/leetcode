from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0] == coordinates[1][0]:
            return all([coordinate[0] == coordinates[0][0] for coordinate in coordinates[2:]])
        if coordinates[0][1] == coordinates[1][1]:
            return all([coordinate[1] == coordinates[0][1] for coordinate in coordinates[2:]])
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        for coordinate in coordinates[2:]:
            y = coordinate[1] - coordinates[0][1]
            x = coordinate[0] - coordinates[0][0]
            if y * dx != x * dy:
                return False
        return True

if __name__=="__main__":
    solution = Solution()
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    print(solution.checkStraightLine(coordinates))