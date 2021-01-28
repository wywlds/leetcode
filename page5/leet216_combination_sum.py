from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        def dfs(tmp, sumn, start):
            if sumn > n or len(tmp) > k:
                return
            if sumn == n and len(tmp) == k:
                self.ans.append(tmp[:])
                return
            for i in range(start, 10):
                tmp.append(i)
                sumn += i
                dfs(tmp, sumn, i + 1)
                tmp.pop()
                sumn -= i
        dfs([], 0, 1)
        return self.ans

if __name__=="__main__":
    solution = Solution()
    print(solution.combinationSum3(3, 10))