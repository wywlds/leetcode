from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        num = 1
        delta = k
        sign = 1
        seq = [1]
        while delta != 0:
            num = num + sign * delta
            sign = -sign
            delta -= 1
            seq.append(num)
        seq.extend(list(range(k + 2, n + 1)))
        return seq