from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        ans[0] = 0
        ans[1] = 1
        base_digit = 1
        for i in range(2, num + 1):
            if i == (1 << (base_digit + 1)):
                base_digit += 1
            ans[i] = 1 + ans[i % (1 << (base_digit))]
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.countBits(8))