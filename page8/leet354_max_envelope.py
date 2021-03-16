from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        N = len(envelopes)
        if N == 0:
            return 0
        next_nodes = [[] for _ in range(N)]
        pre_nodes = [0] * N
        for i in range(N):
            for j in range(i + 1, N):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    next_nodes[i].append(j)
                    pre_nodes[j] += 1
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    next_nodes[j].append(i)
                    pre_nodes[i] += 1
        q = []
        mem = [0] * N
        for i, next_node in enumerate(pre_nodes):
            if next_node == 0:
                q.append((i, 1))
                mem[i] = 1
        while len(q) != 0:
            i, level = q.pop(0)
            for n in next_nodes[i]:
                if mem[n] < level + 1:
                    q.append((n, level+1))
                    mem[n] = level + 1
        return max(mem)


if __name__=="__main__":
    enveloppes = [[5,4],[6,4],[6,7],[2,3]]
    solution = Solution()
    print(solution.maxEnvelopes(enveloppes))