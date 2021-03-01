from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        LEN = len(cars)
        ans = [-1] * LEN
        s = []
        for i in range(LEN-1, -1 ,-1):
            while len(s) > 0:
                if cars[s[-1]][1] >= cars[i][1]:
                    s.pop()
                else:
                    if ans[s[-1]] < 0:
                        break
                    d = ans[s[-1]] * (cars[i][1] - cars[s[-1]][1])
                    if d > (cars[s[-1]][0] - cars[i][0]):
                        break
                    else:
                        s.pop()
            if len(s) == 0:
                ans[i] = -1
            else:
                t = (cars[s[-1]][0] - cars[i][0]) / (cars[i][1] - cars[s[-1]][1])
                ans[i] = t
            s.append(i)
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]))