from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = {}
        for k, v in knowledge:
            dic[k] = v

        ans_mem = []
        temp_mem = []
        for ch in s:
            if ch == "(":
                ans_mem.extend(temp_mem)
                temp_mem = []
            elif ch == ")":
                key = "".join(temp_mem)
                if key in dic:
                    ans_mem.append(dic[key])
                else:
                    ans_mem.append("?")
                temp_mem = []
            else:
                temp_mem.append(ch)
        return "".join(ans_mem)

if __name__=="__main__":
    s = "(a)(b)"
    knowledge = [["a","b"],["b","a"]]
    solution = Solution()
    print(solution.evaluate(s, knowledge))