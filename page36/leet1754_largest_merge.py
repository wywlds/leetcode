class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        LEN = len(word1) + len(word2)
        chr1 = list(word1)
        chr1.append(chr(ord('a') - 1))
        chr2 = list(word2)
        chr2.append(chr(ord('a') - 1))
        i, j, k = 0, 0, 0
        ans_chrs = []
        while i < LEN:
            if chr1[j:] > chr2[k:]:
                ans_chrs.append(chr1[j])
                j += 1
            else:
                ans_chrs.append(chr2[k])
                k += 1
            i = len(ans_chrs)
        return "".join(ans_chrs)


if __name__=="__main__":
    word1 = "uuurruuuruuuuuuuuruuuuu"
    word2 = "urrrurrrrrrrruurrrurrrurrrrruu"
    solution = Solution()
    print(solution.largestMerge(word1, word2))