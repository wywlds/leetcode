import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fraction_re = re.compile("\d+/\d+")
        fs = fraction_re.split(expression)
        fs = fs[1:-1]

        if expression.startswith("-"):
            fs.insert(0, '-')
            expression = expression[1:]
        else:
            fs.insert(0, "+")

        mothers = []
        children = []
        fractions = fraction_re.findall(expression)
        for fraction in fractions:
            items = fraction.split("/")
            mother = int(items[1])
            child = int(items[0])
            mothers.append(mother)
            children.append(child)

        mother = mothers[0]
        for num in mothers[1:]:
            mother = self.lcm(mother, num)

        child = 0
        for f, c, m in zip(fs, children, mothers):
            if f == '+':
                child += c * mother // m
            else:
                child -= c * mother // m

        abs_child = abs(child)
        gcd_value = self.gcd(abs_child, mother)

        return str(child//gcd_value)+"/"+str(mother//gcd_value)

    def gcd(self, a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)


if __name__=="__main__":
    solution = Solution()
    print(solution.fractionAddition("-1/2+1/2+1/3"))