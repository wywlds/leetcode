from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_count = len(rooms)
        visited = [False] * room_count
        q = deque()
        q.append(0)
        while q:
            cur = q.popleft()
            visited[cur] = True
            for next in rooms[cur]:
                if not visited[next]:
                    q.append(next)
        return all(visited)