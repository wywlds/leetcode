class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_parts, b_parts = a.split("+"), b.split("+")
        a_real, b_real = int(a_parts[0]), int(b_parts[0])
        a_virtual, b_virtual = int(a_parts[1].rstrip('i')), int(b_parts[1].rstrip('i'))
        real = a_real * b_real - a_virtual * b_virtual
        virtual = a_real * b_virtual + b_real * a_virtual
        return "%d+%di" % (real, virtual)


if __name__=="__main__":
    solution = Solution()
    print(solution.complexNumberMultiply("1+1i", "1+-1i"))
    print(solution.complexNumberMultiply("1+-1i", "1+-1i"))

