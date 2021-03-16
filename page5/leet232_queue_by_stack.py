class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left_stack = []
        self.right_stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.left_stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.right_stack) == 0:
            while len(self.left_stack) != 0:
                self.right_stack.append(self.left_stack.pop())
        return self.right_stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.right_stack) == 0:
            while len(self.left_stack) != 0:
                self.right_stack.append(self.left_stack.pop())
        return self.right_stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.right_stack) == 0 and len(self.left_stack) == 0