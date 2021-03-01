from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        start = 0
        for i in range(1, len(arr)):
            if (i == 1 and arr[i] != arr[i - 1]) or (arr[i] > arr[i - 1] and arr[i - 1] < arr[i - 2]) or\
                    (arr[i] < arr[i - 1] and arr[i - 1] > arr[i - 2]):
                ans = max(i - start + 1, ans)
            else:
                start = i - 1
        return ans


if __name__=="__main__":
    l = [9,4,2,10,7,8,8,1,9]
    solution = Solution()
    print(solution.maxTurbulenceSize(l))