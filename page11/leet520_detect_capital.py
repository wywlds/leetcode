import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        re1 = re.compile("^[A-Z]+$")
        re2 = re.compile("^[A-Z][a-z]+$")
        re3 = re.compile("^[a-z]+$")

        if re1.findall(word):
            return True
        if re2.findall(word):
            return True
        if re3.findall(word):
            return True
        return False


if __name__=="__main__":
    solution = Solution()
    print(solution.detectCapitalUse("FLAG"))
    print(solution.detectCapitalUse("FLaG"))
    print(solution.detectCapitalUse("Facebook"))
    print(solution.detectCapitalUse("FAcebook"))
    print(solution.detectCapitalUse("facebook"))
