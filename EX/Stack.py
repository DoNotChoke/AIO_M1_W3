class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list = []

    def is_empty(self):
        if (len(self.__list) == 0):
            return True
        return False

    def is_full(self):
        if (len(self.__list) == self.__capacity):
            return True
        return False

    def pop(self):
        # if (self.is_empty()):
        #     return
        num = self.__list[-1]
        self.__list.pop(-1)
        return num

    def push(self, value):
        if (self.is_full()):
            return
        self.__list.append(value)

    def top(self):
        if (self.is_empty()):
            return
        return self.__list[-1]
    def a(self):
        for i in self.__list:
            print(i)


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
