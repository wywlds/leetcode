from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        ch, lc = c.most_common(1)[0]
        if lc > (len(S) + 1) // 2:
            return ""
        ns = [""] * len(S)
        def assign(cnt, ch_s):
            first_round = cnt * 2
            if cnt + 1 > (len(S)+1)//2:
                delta = cnt + 1 - (len(S)+1) // 2
                ns[2*delta - 1] = ch_s
            else:
                ns[first_round] = ch_s
        count = 0
        for _ in range(lc):
            assign(count, ch)
            count += 1

        for nch, chc in c.items():
            if nch == ch:
                continue
            for _ in range(chc):
                assign(count, nch)
                count += 1
        return "".join(ns)


if __name__=="__main__":
    solution = Solution()
    print(solution.reorganizeString("aaabbb"))
    print(solution.reorganizeString("aaabb"))