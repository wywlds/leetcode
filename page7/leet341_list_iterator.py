class NestedInteger:
    pass
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.s = nestedList[::-1]

    def next(self) -> int:
        return self.s.pop().getInteger()


    def hasNext(self) -> bool:
        while len(self.s) != 0 and not self.s[-1].isInteger():
            l = self.s.pop()
            self.s.extend(l.getList()[::-1])
        return len(self.s) != 0