class Queue():
    def __init__(self):
        self.__items = []

    def enqueue(item):
        self.__items.append(item)

    def dequeue(self):
        self.__items.pop(-1)

    def display(self):
        print(self.__items)

q = Queue()
q.display()
q.enqueue(5)
q.enqueue(3)
q.enqueue(2)
q.display()
d.dequeue()
q.display()
