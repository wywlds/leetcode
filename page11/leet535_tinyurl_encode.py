import random
class Codec:
    map = {}
    words = "1234567890abcdefghijklmnopqrstuvwxyz"

    def random_str(self):
        result = ""
        for _ in range(6):
            result += self.words[random.randint(0, len(self.words) - 1)]
        return result

    def encode(self, longUrl: str) -> str:
        short_url = self.random_str()
        while short_url in self.map:
            short_url = self.random_str()
        self.map[short_url] = longUrl
        return "http://tinyurl.com/"+short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        short_url = shortUrl[19:]
        return self.map[short_url]


if __name__=="__main__":
    codec = Codec()
    shortUrl = codec.encode("http://testurl")
    print(shortUrl)
    longurl = codec.decode(shortUrl)
    print(longurl)