from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        counter = {}
        max_count = 0
        for layer in wall:
            agg_length = 0
            for leng in layer[0:len(layer) - 1]:
                agg_length += leng
                if agg_length in counter:
                    count = counter[agg_length] + 1
                    counter[agg_length] = count
                else:
                    counter[agg_length] = 1
                    count = 1
                max_count = max(max_count, count)
        return height - max_count