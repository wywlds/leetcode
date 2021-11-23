from collections import deque
import bisect
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.s = 0
        self.l = []
        self.c = 0
        self.mq = deque()

    def addElement(self, num: int) -> None:
        self.c += 1
        self.s += num
        self.mq.append(num)
        bisect.insort(self.l, num)
        if self.c > self.m:
            poped = self.mq.popleft()
            self.s -= poped
            self.l.pop(bisect.bisect_left(self.l, poped))

    def calculateMKAverage(self) -> int:
        if self.c < self.m:
            return -1
        return int((self.s - sum(self.l[:self.k]) - sum(self.l[self.m -self.k:])) / (self.m - 2 * self.k))


if __name__=="__main__":
    obj = MKAverage(3, 1)
    # obj.addElement(3)
    # obj.addElement(1)
    # print(obj.calculateMKAverage())
    # obj.addElement(10)
    # print(obj.calculateMKAverage())
    obj.addElement(3)
    obj.addElement(1)
    obj.addElement(10)
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    print(obj.calculateMKAverage())