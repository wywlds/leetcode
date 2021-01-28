from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def calculate_key(p):
            return p[0] * 1000 - p[1]
        people.sort(key=calculate_key)
        ans = [None] * len(people)
        for p in people:
            N = p[1]
            empty = 0
            for i in range(len(people)):
                if ans[i] is None:
                    if empty == N:
                        ans[i] = p
                        break
                    empty += 1
        return ans


if __name__=="__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    solution = Solution()
    solution.reconstructQueue(people)