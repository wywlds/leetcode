class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenMap = {}


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenMap[tokenId] = currentTime


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenMap:
            lastTime = self.tokenMap[tokenId]
            if currentTime < lastTime + self.timeToLive:
                self.tokenMap[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for k, t in self.tokenMap:
            if currentTime < t + self.timeToLive:
                cnt += 1
        return cnt