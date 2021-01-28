class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
        for move in moves:
            counter[move] += 1
        return counter['R'] == counter['L'] and counter['U'] == counter['D']