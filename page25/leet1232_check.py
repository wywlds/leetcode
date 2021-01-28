from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return all((coordinates[1][0] - coordinates[0][0])*(y - coordinates[0][1]) == (coordinates[1][1] - coordinates[0][1])* (x - coordinates[0][0])
                   for x,y in coordinates[2:])


if __name__=="__main__":
    solution = Solution()
    print(solution.checkStraightLine([[0, 0], [1, 0], [0, 1]]))