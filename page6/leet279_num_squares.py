import math
class Solution:
    def numSquares(self, n: int) -> int:
        mem = [float('inf')] * (n + 1)
        mem[0] = 0
        for i in range(int(math.sqrt(n)), 0, -1):
            for j in range(i * i, n + 1):
                mem[j] = min(mem[j], mem[j - i * i] + 1)
            if mem[n] <= n:
                return mem[n]
        return mem[n]