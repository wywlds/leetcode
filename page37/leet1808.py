class Solution:
    def pow_in(self, num):
        if num == 1:
            return 3
        BASE = 10**9 + 7
        if num % 2 == 0:
            ans = self.pow_in(num // 2) ** 2
        else:
            ans = self.pow_in(num // 2) ** 2 * 3
        return ans % BASE

    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors == 0:
            return 0
        if primeFactors == 1:
            return 0
        if primeFactors == 2:
            return 1
        if primeFactors == 3:
            return 2
        num3 = primeFactors // 3
        residu3 = primeFactors % 3

        BASE = 10**9 + 7
        if residu3 == 0:
            pow()
            return self.pow_in(num3) % BASE
        elif residu3 == 1:
            return self.pow_in(num3 - 1) * 4 % BASE
        elif residu3 == 2:
            return self.pow_in(num3) * 2 % BASE