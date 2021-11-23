class Solution:
    def clumsy(self, N: int) -> int:
        value_list = []
        i = N
        while i > 0:
            if i >= 3:
                value_list.append([i, i - 1, i - 2])
                i -= 3
            elif i == 2:
                value_list.append([i, i - 1])
                i -= 2

            if i >= 1:
                value_list.append([i])
                i -= 1
        def cal(values):
            if len(values) == 3:
                return int(values[0] * values[1] / values[2])
            elif len(values) == 2:
                return values[0] * values[1]
            else:
                return values[0]
        ans = cal(value_list[0])
        positive = True
        for values in value_list[1:]:
            if positive:
                ans += cal(values)
            else:
                ans -= cal(values)
            positive = not positive
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.clumsy(10))