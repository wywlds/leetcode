from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        agg = 0
        for enc in range(1, len(encoded) + 2):
            agg ^= enc
        perm = [0] * (len(encoded) + 1)
        perm[0] = agg
        for i in range(1, len(encoded), 2):
            perm[0] ^= encoded[i]
        for i in range(1, len(perm)):
            perm[i] = perm[i- 1] ^ encoded[i - 1]
        return perm

if __name__=="__main__":
    solution = Solution()
    print(solution.decode([3,1]))