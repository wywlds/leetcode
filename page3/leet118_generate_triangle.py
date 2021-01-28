from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        while len(ans) < numRows:
            last_array = ans[-1]
            new_array = [1]
            for a, b in zip(last_array[:-1], last_array[1:]):
                new_array.append(a + b)
            new_array.append(1)
            ans.append(new_array)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.generate(10))