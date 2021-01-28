class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        count_L = 0
        for ch in s:
            if ch == 'A':
                count_L = 0
                count_A += 1
                if count_A > 1:
                    return False
            elif ch == 'L':
                count_L += 1
                if count_L > 2:
                    return False
            else:
                count_L = 0
        return True
