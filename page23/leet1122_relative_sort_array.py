from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_dic = {}
        for i, num in enumerate(arr2):
            arr2_dic[num] = i
        def sort_key(v):
            if v in arr2_dic:
                return arr2_dic[v] - 1000
            else:
                return v

        arr1.sort(key=sort_key)
        return arr1