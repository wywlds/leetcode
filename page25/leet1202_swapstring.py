from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ans_l = list(s)
        disj = [-1] * len(s)
        def find(i):
            if disj[i] < 0:
                return i
            disj[i] = find(disj[i])
            return disj[i]
        def union(i, j):
            p_i = find(i)
            p_j = find(j)
            if p_i == p_j:
                return
            if p_i < p_j:
                disj[p_j] = p_i
            else:
                disj[p_i] = p_j
        for p1, p2 in pairs:
            union(p1, p2)
        dic = {}
        for i in range(len(s)):
            r = find(i)
            if r not in dic:
                dic[r] = [[i], [s[i]]]
            else:
                dic[r][0].append(i)
                dic[r][1].append(s[i])
        for _, (indexes, values) in dic.items():
            values.sort()
            for i in range(len(indexes)):
                ans_l[indexes[i]] = values[i]
        return "".join(ans_l)


if __name__=="__main__":
    solution = Solution()
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    print(solution.smallestStringWithSwaps(s, pairs))