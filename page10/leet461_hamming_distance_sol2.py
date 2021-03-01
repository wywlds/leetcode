class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        for i in range(32):
            if (x & (1 << i)) ^ (y & (1 << i)):
                ans += 1
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.hammingDistance(1, 4))
    print(solution.hammingDistance(1, 3))