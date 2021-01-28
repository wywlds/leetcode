from typing import List

import random


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.mapping = {}
        self.flip_cnt = 0
        self.total_cnt = n_rows * n_cols
        self.n_rows = n_rows


    def flip(self) -> List[int]:
        if self.flip_cnt >= self.total_cnt:
            return []
        max_pos = self.total_cnt - self.flip_cnt
        cur = random.randint(0, max_pos - 1)
        res = cur
        while res in self.mapping:
            res = self.mapping[res]
        self.mapping[cur] = max_pos - 1
        self.flip_cnt += 1
        return [res // self.n_rows, res % self.n_rows]

    def reset(self) -> None:
        self.mapping.clear()
        self.flip_cnt = 0


if __name__=="__main__":
    solution = Solution(2, 2)
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
    solution.reset()
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
    print(solution.flip())
