import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        reg = re.compile("[+-]*[\dx]+")
        left = equation.split("=")[0]
        right = equation.split("=")[1]
        lefts = reg.findall(left)
        rights = reg.findall(right)
        vars = [0, 0]
        for left in lefts:
            a, b = self.parse(left)
            vars = [vars[0] + a, vars[1] + b]
        for right in rights:
            a, b = self.parse(right)
            vars = [vars[0] - a, vars[1] - b]
        if vars[0] != 0:
            return "x=" + str(int(-vars[1]/vars[0]))
        else:
            if vars[1] == 0:
                return "Infinite solutions"
            else:
                return "No solution"

    def parse(self, v_str):
        if v_str.endswith("x"):
            if (v_str.startswith("+") or v_str.startswith("-")) and len(v_str) == 2:
                v_str = v_str[:-1] + "1" + v_str[-1]
            if len(v_str) > 1:
                var = int(v_str[:-1])
            else:
                var = 1
            return [var, 0]
        return [0, int(v_str)]


if __name__=="__main__":
    solution = Solution()
    print(solution.solveEquation("x+5-3+x=6+x-2"))