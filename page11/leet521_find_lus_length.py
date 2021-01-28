class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) < len(b):
            return self.findLUSlength(b, a)
        def check(a, b):
            if len(a) > len(b):
                return False
            loc = -1
            for c in a:
                loc = b.find(c, loc+1)
                if loc == -1:
                    return False
            return True
        if not check(a, b):
            return len(a)
        if not check(b, a):
            return len(b)
        return -1

if __name__=="__main__":
    solution = Solution()
    print(solution.findLUSlength("ab", "aaa"))