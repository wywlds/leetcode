class Solution:
    def findIntegers(self, num: int) -> int:
        f, f[0], f[1] = [0] * 32, 1, 2
        for i in range(2, 32):
            f[i] = f[i-1] + f[i - 2]
        i, sum, pre_bit = 30, 0, 0
        while i >= 0:
            bit = num & (1 << i)
            if bit != 0:
                sum += f[i]
                if pre_bit != 0:
                    return sum
                pre_bit = 1
            else:
                pre_bit = 0
            i -= 1
        return sum +1

