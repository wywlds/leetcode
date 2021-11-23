class Solution:
    def reverseBits(self, n: int) -> int:
        print("%x" % n)
        M1 = 0x55555555
        M2 = 0x33333333
        M3 = 0x0f0f0f0f
        M4 = 0x00ff00ff
        M5 = 0xffffffff
        n = ((n >> 1 & M1) & M5) | ((n & M1) << 1 & M5)
        print("%x" % n)
        n = ((n >> 2 & M2) & M5) | ((n & M2) << 2 & M5)
        print("%x" % n)
        n = ((n >> 4 & M3) & M5) | ((n & M3) << 4 & M5)
        print("%x" % n)
        n = ((n >> 8 & M4) & M5) | ((n & M4) << 8 & M5)
        print("%x" % n)
        return (n << 16 & M5) | (n >> 16 & M5)

if __name__=="__main__":
    solution = Solution()
    solution.reverseBits(0xfffffffd)