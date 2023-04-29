class MyCircularDeque:
    def __init__(self, k: int):
        self.dummy = -1
        self.max_len = k
        self.cirqueue = [self.dummy for _ in range(self.max_len)]
        self.front, self.rear = 0, 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear - 1) % self.max_len
            self.cirqueue[self.rear] = value
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.cirqueue[self.front] = value
            self.front = (self.front + 1) % self.max_len
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.cirqueue[self.rear] = self.dummy
            self.rear = (self.rear + 1) % self.max_len
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front - 1) % self.max_len
            self.cirqueue[self.front] = self.dummy
            self.size -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.cirqueue[self.rear]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.cirqueue[self.front]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.size == 0

    def isFull(self) -> bool:
        return self.front == self.rear and self.size == self.max_len

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()