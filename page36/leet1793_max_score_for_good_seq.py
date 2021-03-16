from typing import List


class Solution:
    def get_K_len(self, seq, K):
        LEN = len(seq)
        ans = [LEN] * K
        for i in range(LEN-1, -1 ,-1):
            if seq[i] < K:
                ans[seq[i]] = i
        for i in range(1, K):
            ans[i] = min(ans[i], ans[i - 1])
        return ans

    def maximumScore(self, nums: List[int], k: int) -> int:
        K = nums[k]
        left_seq = nums[:k][::-1]
        right_seq = nums[k + 1:]
        left_len = self.get_K_len(left_seq, K)
        right_len = self.get_K_len(right_seq, K)
        ans = -1
        for i, (left, right) in enumerate(zip(left_len, right_len)):
            min_val = i + 1
            len = left + right + 1
            ans = max(ans, min_val * len)
        return ans


if __name__=="__main__":
    nums = [5,5,4,5,4,1,1,1]
    k = 0
    solution = Solution()
    print(solution.maximumScore(nums, 4))