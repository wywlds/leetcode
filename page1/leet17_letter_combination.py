from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = ["","","abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        last_list = [""]
        for i, digit in enumerate(digits):
            new_list = []
            for last_str in last_list:
                keys = keyboard[int(digit)]
                for next_ch in keys:
                    new_list.append(last_str + next_ch)
            last_list = new_list
        return last_list


if __name__=="__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))