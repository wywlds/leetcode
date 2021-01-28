class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        pos = [0] * 10
        def ord_ch(ch):
            return ord(ch) - ord('0')
        for i, ch in enumerate(num_str):
            pos[ord_ch(ch)] = i

        for i, ch in enumerate(num_str):
            for cand in range(9, ord_ch(ch), -1):
                if pos[cand] > i:
                    ch_list = list(num_str)

                    ch_list[i] = cand
                    ch_list[pos[cand]] = ch
                    return int("".join(ch_list))

        return num
