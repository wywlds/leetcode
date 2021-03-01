from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sls = [0]
        s1 = 0
        for num in cardPoints[0:k]:
            s1 += num
            sls.append(s1)
        srs = [0]
        s2 = 0
        for num in cardPoints[::-1][0:k]:
            s2 += num
            srs.append(s2)
        ans = 0
        for l, r in zip(sls, srs[::-1]):
            ans = max(ans, l + r)
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.maxScore([1,23,4,2,3,5,12,2], 3))