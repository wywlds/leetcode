from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        len_map = {}
        stack = []
        for i, num in enumerate(nums):
            if i not in len_map:
                len_map[i] = 0
                stack.append(i)
                while True:
                    if num not in len_map:
                        len_map[num] = 0
                        stack.append(num)
                        num = nums[num]
                    else:
                        base = len_map[num]
                        while stack:
                            num = stack.pop()
                            len_map[num] = base + 1
                            base += 1
                        break
        return max(len_map.values())


if __name__=="__main__":
    A = [5, 4, 0, 3, 1, 6, 2]
    solution = Solution()
    print(solution.arrayNesting(A))