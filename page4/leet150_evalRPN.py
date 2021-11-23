from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        def handle(op, v1, v2):
            if op == '+':
                return v1 + v2
            elif op == '-':
                return v1 - v2
            elif op == '*':
                return v1 * v2
            else:
                return v1 / v2
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                v2 = s.pop()
                v1 = s.pop()
                s.append(handle(token, v1, v2))
            else:
                s.append(int(token))
        return s[-1]