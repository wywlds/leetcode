class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord('a')
        y = int(coordinates[1])
        return (x + y) % 2 == 1