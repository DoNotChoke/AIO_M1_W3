class MyQueue:
    def __init__(self, capacity):
        self.__list = []
        self.__capacity = capacity

    def is_empty(self):
        if (len(self.__list) == 0):
            return True
        return False

    def is_full(self):
        if (len(self.__list) == self.__capacity):
            return True
        return False

    def dequeue(self):
        if (self.is_empty()):
            return
        num = self.__list[0]
        self.__list.pop(0)
        return num

    def enqueue(self, value):
        if (self.is_full()):
            return
        self.__list.append(value)

    def front(self):
        if (self.is_empty()):
            return
        return self.__list[0]

queue1 = MyQueue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())