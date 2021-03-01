class Solution:
    """
    采用布莱恩-克尼根算法
    """
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ans = 0
        while xor:
            ans += 1
            xor = xor & (xor - 1)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.hammingDistance(1, 4))
    print(solution.hammingDistance(1, 3))