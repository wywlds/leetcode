from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        pq = []
        rights = [len(heights) for _ in range(len(heights))]
        lefts = [-1 for _ in range(len(heights))]
        for i in range(len(heights)):
            while len(pq) > 0 and heights[pq[-1]] >= heights[i]:
                j = pq.pop()
                rights[j] = i
            lefts[i] = pq[-1] if len(pq) > 0 else -1
            pq.append(i)
        ans = max([(rights[i] - lefts[i] - 1) * heights[i] for i in range(len(heights))])
        return ans

if __name__=="__main__":
    solution = Solution()
    heights = [2,1,5,6,2,3]
    print(solution.largestRectangleArea(heights))