from typing import List
import collections


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        counter = collections.Counter()
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord('a')))
            if bin(mask).count('1') <= 7:
                counter[mask] += 1
        ans = []
        for puzzle in puzzles:
            base_mask = 0
            for p in puzzle[1:]:
                base_mask |= (1 << (ord(p) - ord('a')))
            count = 0
            subset = base_mask
            while subset:
                s = subset | (1 << ord(puzzle[0]) - ord('a'))
                count += counter[s]
                subset = (subset - 1) & base_mask
            count += counter[1 << (ord(puzzle[0]) - ord('a'))]
            ans.append(count)
        return ans

    def get_subsets(self, bitmask):
        subset = bitmask
        ans = [bitmask]
        while subset != 0:
            subset = bitmask & (subset - 1)
            ans.append(subset)
        return ans


if __name__=="__main__":
    words = ["aaaa","asas","able","ability","actt","actor","access"]
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    solution = Solution()
    ans = solution.findNumOfValidWords(words, puzzles)
    print(ans)