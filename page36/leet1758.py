class Solution:
    def minOperations(self, s: str) -> int:
        a1, a2 = 0, 0
        for i, ch in enumerate(s):
            if (i % 2 == 0 and ch == '0') or (i % 2 == 1 and ch == '1'):
                a1 += 1
            if (i % 2 == 0 and ch == '1') or (i % 2 == 1 and ch == '0'):
                a2 += 1
        return min(a1, a2)


if __name__=="__main__":
    solution = Solution()
    print(solution.minOperations("1111"))