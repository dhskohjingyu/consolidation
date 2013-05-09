class LinkedNode():
    def __init__(self, value):
        self.__value = value
        self.__pointer = None

    def set_value(self, new_value):
        self.__value = new_value

    def get_value(self):
        return self.__value

    def set_pointer(self, new_pointer):
        self.__pointer = new_pointer

    def get_pointer(self):
        return self.__pointer

class LinkedList():
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_value(self, value):
        new = LinkedNode(value)

        if self.__head == None:
            self.__head = new

        if self.__tail != None:
            self.__tail.set_pointer(new)

        self.__tail = new

    def remove_node(self, index):
        node = self.__head
        previous_node = None
        count = 0

        while count < index:
            previous_node = node
            node = self.__head.get_pointer()
            count += 1

        if node == None:
            print("IndexError: stack index out of range")
        else:
            next_node = node.get_pointer()
            
            if previous_node == None:
                # removing the head
                self.__head = next_node
            else:
                previous_node.set_pointer(next_node)

            if next_node == None:
                # removing the tail
                self.__tail = previous_node
            else:
                previous_node.set_pointer(None)
                
            node = None

    def display(self):
        node = self.__head

        while node:
            print(node.get_value())
            node = node.get_pointer()

l = LinkedList()
l.add_value(2)
l.add_value(3)
l.add_value(5)
l.display()
print("--------")
l.remove_node(2)
l.display()
