from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def num_max(num1, num2):
            if len(num1) > len(num2):
                return num1
            elif len(num2) > len(num1):
                return num2
            else:
                return max(num1, num2)

        mem = [[-1] for _ in range(target + 1)]
        for i, c in enumerate(cost):
            num = i + 1
            if c > target:
                continue
            mem[c] = num_max(mem[c], [num])
            for j in range(c + 1, target + 1):
                if mem[j - c][0] != -1:
                    new_num = [num, *mem[j - c]]
                    mem[j] = num_max(mem[j], new_num)
        if mem[target][0] == -1:
            return 0
        else:
            return "".join([str(i) for i in mem[target]])

if __name__=="__main__":
    cost = [2,4,6,2,4,6,4,4,4]
    target = 5
    solution = Solution()
    print(solution.largestNumber(cost, target))
