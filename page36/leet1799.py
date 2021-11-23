from typing import List


class Solution:
    def gcd(self, a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def maxScore(self, nums: List[int]) -> int:
        LEN = len(nums)
        gcds = []
        for i in range(LEN):
            for j in range(i + 1, LEN):
                gcds.append((self.gcd(nums[i], nums[j]), i, j))

        gcds.sort(reverse=True)
        ans = 0
        aggs = [1, 3, 6, 10, 15, 21, 28]
        def dfs(i, cnt, occupied, cur_sum):
            nonlocal LEN, ans
            if cnt == 0 or i == len(gcds) - cnt + 1:
                return
            gcd, i2, j = gcds[i]

            if (cur_sum + aggs[cnt - 1] * gcd) <= ans:
                return
            if not ((1 << i2) & occupied) and not ((1 << j) & occupied):
                new_occupied = (occupied | (1 << i2) | (1 << j))
                cur_sum_2 = cur_sum + cnt * gcd
                ans = max(ans, cur_sum_2)
                dfs(i + 1, cnt - 1, new_occupied, cur_sum_2)
            dfs(i + 1, cnt, occupied, cur_sum)
        dfs(0, LEN // 2, 0, 0)
        return ans

if __name__=="__main__":
    l = [1,2,3,4,5,6]
    solution = Solution()
    print(solution.maxScore([1,2,3,4,5,6]))