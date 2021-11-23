import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        splits = re.split("[a-zA-Z]+", word)
        nums = []
        for split in splits:
            if split.isnumeric():
                nums.append(int(split))
        return len(set(nums))

if __name__=="__main__":
    solution = Solution()
    print(solution.numDifferentIntegers("a1b01c001"))