class CQueue:

    def __init__(self):
        self.queue_input = []
        self.queue_output = []


    def appendTail(self, value: int) -> None:
        self.queue_input.append(value)


    def deleteHead(self) -> int:
        if not self.queue_output:
            while self.queue_input:
                self.queue_output.append(self.queue_input.pop())
        if self.queue_output:
            return self.queue_output.pop()
        else:
            return -1


if __name__=="__main__":
    cqueue = CQueue()
    cqueue.appendTail(3)
    print(cqueue.dele)