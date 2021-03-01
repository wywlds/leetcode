from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        LEN1 = len(nums1)
        LEN2 = len(nums2)
        if LEN1 > LEN2 * 6 or LEN2 > LEN1 * 6:
            return -1
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 > sum2:
            larger = nums1
            smaller = nums2
        elif sum1 < sum2:
            larger = nums2
            smaller = nums1
        else:
            return 0

        larger.sort(reverse=True)
        smaller.sort()
        delta = abs(sum1 - sum2)
        count = 0
        l, s = 0, 0
        while delta > 0:
            d1 = larger[l] - 1 if l < len(larger) else 0
            d2 = 6 - smaller[s] if s < len(smaller) else 0
            if d1 > d2:
                delta -= d1
                l += 1
            else:
                delta -= d2
                s += 1
            count += 1
        return count


if __name__=="__main__":
    nums1 = [1,2,3,4,5,6]
    nums2 = [1,1,2,2,2,2]
    solution = Solution()
    print(solution.minOperations(nums1, nums2))