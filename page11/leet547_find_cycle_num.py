from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        p_num = len(M)
        upstreams = [-1] * p_num
        def get_root(i):
            while upstreams[i] != -1:
                up_k = upstreams[i]
                i = up_k
            return i
        for i in range(0, p_num - 1):
            for j in range(i + 1, p_num):
                if M[i][j] == 1:
                    root_i = get_root(i)
                    root_j = get_root(j)
                    if i != j:
                        upstreams[root_j] = root_i
        count = 0
        for upstream in upstreams:
            if upstream == -1:
                count += 1
        return count