class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.q = [0] * k
        self.head = 0
        self.tail = 1
        self.leng = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.q[self.head] = value
        self.head = (self.head - 1) % len(self.q)
        self.leng += 1
        return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % len(self.q)
        self.leng += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.q)
        self.leng -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % len(self.q)
        self.leng -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        head = (self.head + 1) % len(self.q)
        return self.q[head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        tail = (self.tail - 1) % len(self.q)
        return self.q[tail]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.leng == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.leng == len(self.q)


if __name__=="__main__":
    circular_queue = MyCircularDeque(3)
    circular_queue.insertLast(1)
    circular_queue.insertLast(2)
    circular_queue.insertFront(3)
    print(circular_queue.getRear())