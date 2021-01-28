from typing import List
import collections
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        def dfs(pos):
            while map[pos]:
                next = heapq.heappop(map[pos])
                dfs(next)
            ans.append(pos)

        map = collections.defaultdict(list)
        for start, end in tickets:
            map[start].append(end)
        for value in map.values():
            heapq.heapify(value)
        dfs('JFK')
        return ans[::-1]


if __name__=="__main__":
    solution = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(solution.findItinerary(tickets))