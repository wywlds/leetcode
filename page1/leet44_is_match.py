class Solution:
    memory = {}
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0 and len(s) == 0:
            return True
        if p == '*':
            return True
        if len(p) == 0:
            return len(s) == 0
        if (s, p) in self.memory:
            return self.memory[(s, p)]
        i = 0
        if p[i] == '*':
            while i < len(p) and p[i] == '*':
                i += 1
            is_match = self.isMatch(s[1:], p[i-1:]) or self.isMatch(s, p[i:])
            self.memory[(s, p)] = is_match
            return is_match
        if p[0] == '?' or s[0] == p[0]:
            return self.isMatch(s[1:], p[1:])
        self.memory[(s, p)] = False
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.isMatch("aa", "*"))