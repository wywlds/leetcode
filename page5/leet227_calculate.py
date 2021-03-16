class Solution:
    def calculate(self, s: str) -> int:

        sign = True
        opees = []
        op = ""

        def clear():
            nonlocal op
            if op != "":
                p1 = opees.pop()
                p2 = opees.pop()
                if op == "*":
                    opees.append(p1 * p2)
                else:
                    opees.append(int(p2 / p1))
                op = ""
        for i, ch in enumerate(s):
            if ch == " ":
                continue
            elif ch in ['+', '-']:
                clear()
                sign = (ch == '+')
            elif ch in ['*', '/']:
                clear()
                op = ch
            else:
                if i != 0 and s[i-1].isdigit():
                    base = opees.pop()
                    if base < 0:
                        base = base * 10 - int(ch)
                    else:
                        base = base * 10 + int(ch)
                    opees.append(base)
                else:
                    if sign:
                        opees.append(int(ch))
                    else:
                        opees.append(-int(ch))
                    sign = True
        clear()
        return sum(opees)

if __name__=="__main__":
    solution = Solution()
    print(solution.calculate("3+2*2"))
    print(solution.calculate(" 3/2 "))
    print(solution.calculate(" 3+5 / 2 "))
    print(solution.calculate("12-3*4"))
    print(solution.calculate("14/3*2")) # 8
    print(solution.calculate("1*2-3/4+5*6-7*8+9/10")) # -24