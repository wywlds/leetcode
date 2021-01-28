from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return [0]
        if shorter == longer:
            return shorter * k
        result = []
        for i in range(k + 1):
            result.append(i * longer + (k - i) * shorter)
        return result