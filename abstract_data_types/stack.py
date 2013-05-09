class Stack():
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) > 0:
            self.__items.pop()
        else:
            print("Cannot pop an empty stack.")

    def display(self):
        print(self.__items)


s = Stack()
s.display()
s.push(5)
s.push(2)
s.push(3)
s.display()
s.pop()
s.display()
