class MyCircularQueue:

    def __init__(self, k: int):
        self.dummy = -1
        self.max_len = k
        self.queue = [self.dummy for _ in range(self.max_len)]
        self.front, self.rear = 0, 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.front % self.max_len] = value
            self.front += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.rear % self.max_len] = self.dummy
            self.rear += 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear % self.max_len]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.front - 1) % self.max_len]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.front - self.rear == self.max_len

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()