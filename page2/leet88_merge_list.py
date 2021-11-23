from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p2 = len(nums2) - 1
        p1 = m - 1
        p = len(nums1) - 1
        while p > -1:
            if p1 > -1 and p2 > -1:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p -= 1
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p -= 1
                    p2 -= 1
            elif p1 > -1:
                break
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1


if __name__=="__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)
