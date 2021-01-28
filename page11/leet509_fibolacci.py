class Solution:
    def __init__(self):
        self.nums = [0, 1]
        for i in range(2, 31):
            self.nums.append(self.nums[i-1] + self.nums[i - 2])

    def fib(self, N: int) -> int:
        return self.nums[N]


if __name__ == "__main__":
    solution = Solution()
    for i in range(31):
        print(solution.fib(i))