from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = [-1] * len(stones)
        x_stone_dic = {}
        y_stone_dic = {}
        ans = 0

        def find(x):
            if parents[x] < 0:
                return x
            parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            x_parent = find(x)
            y_parent = find(y)
            if x_parent == y_parent:
                return 0
            parents[y_parent] = x_parent
            return 1

        for i, (stone_x, stone_y) in enumerate(stones):
            if stone_x in x_stone_dic and stone_y in y_stone_dic:
                union(x_stone_dic[stone_x], i)
                ans -= union(x_stone_dic[stone_x], y_stone_dic[stone_y])
            elif stone_x in x_stone_dic:
                union(x_stone_dic[stone_x], i)
                y_stone_dic[stone_y] = i
            elif stone_y in y_stone_dic:
                union(y_stone_dic[stone_y], i)
                x_stone_dic[stone_x] = i
            else:
                x_stone_dic[stone_x] = i
                y_stone_dic[stone_y] = i
                ans += 1
        return len(stones) - ans

if __name__=="__main__":
    stones = [[0,1],[1,0],[1,1]]
    solution = Solution()
    print(solution.removeStones(stones))