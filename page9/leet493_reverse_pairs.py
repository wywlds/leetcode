from typing import List


class Solution:
    def reversePairsInternal(self, nums, l, r):
        if l == r:
            return 0
        else:
            ans = 0
            mid = (l + r) // 2
            ans += self.reversePairsInternal(nums, l, mid)
            ans += self.reversePairsInternal(nums, mid+1, r)

            i = l
            j = mid + 1
            while i <= mid:
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                ans += (j - mid - 1)
                i += 1

            left = nums[l : mid + 1]
            left.append(float('inf'))
            right = nums[mid + 1 : r + 1]
            right.append(float('inf'))
            p1, p2 = 0, 0
            for i in range(l, r + 1):
                if left[p1] < right[p2]:
                    nums[i] = left[p1]
                    p1 += 1
                else:
                    nums[i] = right[p2]
                    p2 += 1
            return ans

    def reversePairs(self, nums: List[int]) -> int:
        ans = self.reversePairsInternal(nums, 0, len(nums)-1)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.reversePairs([2,4,3,5,1]))