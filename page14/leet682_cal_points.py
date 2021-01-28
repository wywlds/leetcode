from typing import List

import re
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        seq = []
        reg = re.compile("^[+-]*[0-9]+$")
        for op in ops:
            if len(reg.findall(op)) > 0:
                seq.append(int(op))
            elif op == '+':
                seq.append(seq[-1] + seq[-2])
            elif op == 'D':
                seq.append(seq[-1] * 2)
            elif op == 'C':
                seq.pop()
        return sum(seq)

if __name__=="__main__":
    solution = Solution()
    print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))