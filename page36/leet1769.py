from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = [0] * len(boxes)
        cnt_left = [0] * len(boxes)
        right = [0] * len(boxes)
        cnt_right = [0] * len(boxes)
        for i in range(0, len(boxes)):
            cnt_left[i] = (cnt_left[i - 1] if i > 0 else 0) + (1 if boxes[i] == '1' else 0)
            if i != 0:
                left[i] = left[i - 1] + cnt_left[i - 1]
        for i in range(len(boxes) - 1, -1, -1):
            cnt_right[i] = (cnt_right[i + 1] if i != len(boxes) - 1 else 0) + (1 if boxes[i] == '1' else 0)
            if i != len(boxes) - 1:
                right[i] = right[i + 1] + cnt_right[i + 1]

        ans = [left[i] + right[i] for i in range(len(boxes))]
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.minOperations("001011"))
