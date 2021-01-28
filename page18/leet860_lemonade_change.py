from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0, 0]
        for bill in bills:
            if bill == 20:
                if counts[1] > 0:
                    if counts[0] == 0:
                        return False
                    counts[1] -= 1
                    counts[0] -= 1
                else:
                    if counts[0] < 3:
                        return False
                    counts[0] -= 3
            elif bill == 10:
                if counts[0] < 1:
                    return False
                counts[0] -= 1
                counts[1] += 1
            else:
                counts[0] += 1
        return True