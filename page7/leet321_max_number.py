from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and (k - i) <= len(nums2):
                max_sub_sequence1 = self.get_max_subsequence(nums1, i)
                max_sub_sequence2 = self.get_max_subsequence(nums2, k - i)
                merged = self.merge(max_sub_sequence1, max_sub_sequence2)
                if self.compare(merged, 0, ans, 0):
                    ans = merged
        return ans

    def get_max_subsequence(self, nums, i):
        if i == 0:
            return []
        else:
            ans = [0] * i
            to_rm_cnt = len(nums) - i
            top = -1
            for num in nums:
                while top >= 0 and ans[top] < num and to_rm_cnt > 0:
                    top -= 1
                    to_rm_cnt -= 1
                if top < i - 1:
                    top += 1
                    ans[top] = num
                else:
                    to_rm_cnt -= 1
            return ans

    def merge(self, seq1, seq2):
        LEN = len(seq1) + len(seq2)
        seq1.append(float('-inf'))
        seq2.append(float('-inf'))
        seq = []
        i, j = 0, 0
        for _ in range(LEN):
            if self.compare(seq1, i, seq2, j):
                seq.append(seq1[i])
                i += 1
            else:
                seq.append(seq2[j])
                j += 1
        return seq

    def compare(self, merged, i1, ans, i2):
        while i1 < len(merged) and i2 < len(ans):
            if merged[i1] > ans[i2]:
                return True
            elif merged[i1] < ans[i2]:
                return False
            i1 += 1
            i2 += 1
        return (len(merged) - i1) > (len(ans) - i2)

if __name__=="__main__":
    seq1 = []
    seq2 = [6,0,4]
    solution = Solution()
    print(solution.maxNumber(seq2, seq1, 3))