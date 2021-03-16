class Solution:
    def calculate(self, s: str) -> int:
        operatees = []
        sig = [True]
        for i, ch in enumerate(s):
            if ch == " ":
                continue
            elif ch == "(":
                sig.append(True)
                operatees.append(ch)
            elif ch == "+":
                sig.append(True)
            elif ch == "-":
                sig.append(False)
            elif ch == ")":
                ans = 0
                while operatees[-1] != '(':
                    p = operatees.pop()
                    ans += p
                operatees.pop()
                si = sig.pop()
                if si:
                    operatees.append(ans)
                else:
                    operatees.append(-ans)
            else:
                if i != 0 and s[i-1].isdigit():
                    base = operatees.pop()
                    if base < 0:
                        base = base * 10 - int(ch)
                    else:
                        base = base * 10 + int(ch)
                    operatees.append(base)
                else:
                    si = sig.pop()
                    if si:
                        operatees.append(int(ch))
                    else:
                        operatees.append(-int(ch))
        return sum(operatees)


if __name__=="__main__":
    solution = Solution()
    # print(solution.calculate("121+5"))
    print(solution.calculate("2-1+2"))
    print(solution.calculate( "(1+(4+5+2)-3)+(6+8)"))
    print(solution.calculate( "1-(6+8)"))
    print(solution.calculate("1-11"))