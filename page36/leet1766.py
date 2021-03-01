from typing import List


class Solution:
    def gcd(self, a, b):
        ta, tb = a, b
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        neibors = [[] for _ in range(len(nums))]
        ans = [-1] * len(nums)
        num_level = [[] for _ in range(51)]
        for s, t in edges:
            neibors[s].append(t)
            neibors[t].append(s)
        def dfs(path, i):
            num_i = nums[i]
            max_level = -1
            for x in range(1, 51):
                if len(num_level[x]) > 0 and self.gcd(x, num_i) == 1 and num_level[x][-1][0] > max_level:
                    ans[i] = num_level[x][-1][1]
                    max_level = num_level[x][-1][0]
            path.append(i)
            num_level[num_i].append((len(path), i))
            for nnum_i in neibors[i]:
                if i == 0 or nnum_i != path[-2]:
                    dfs(path, nnum_i)
            path.pop()
            num_level[num_i].pop()
        dfs([], 0)
        return ans


if __name__=="__main__":
    nums = [9,16,30,23,33,35,9,47,39,46,16,38,5,49,21,44,17,1,6,37,49,15,23,46,38,9,27,3,24,1,14,17,12,23,43,38,12,4,8,17,11,18,26,22,49,14,9]
    edges = [[17,0],[30,17],[41,30],[10,30],[13,10],[7,13],[6,7],[45,10],[2,10],[14,2],[40,14],[28,40],[29,40],[8,29],[15,29],[26,15],[23,40],[19,23],[34,19],[18,23],[42,18],[5,42],[32,5],[16,32],[35,14],[25,35],[43,25],[3,43],[36,25],[38,36],[27,38],[24,36],[31,24],[11,31],[39,24],[12,39],[20,12],[22,12],[21,39],[1,21],[33,1],[37,1],[44,37],[9,44],[46,2],[4,46]]
    solution = Solution()
    print(solution.getCoprimes(nums, edges))

    # [-1, 21, 17, 43, 10, 42, 7, 13, 29, 44, 17, 31, 39, 10, 10, 29, 32, 0, 40, 23, 12, 39, 12, 40, 25, 35, 15, 38, 40, 40, 17, 24, 5, 1, 19, 14, 17, 21, 25, 24, 14, 17, 40, 25, 37, 17, 10]
