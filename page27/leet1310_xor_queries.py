from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        agg = [0]
        cur = 0
        for a in arr:
            cur ^= a
            agg.append(cur)
        ans = []
        for s, e in queries:
            ans.append(agg[s] ^ agg[e + 1])
        return ans


if __name__=="__main__":
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3],[3,3]]
    solution = Solution()
    print(solution.xorQueries(arr, queries))