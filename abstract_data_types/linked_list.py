class LinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.pointer = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head == None:
            self.head = LinkedNode(value)
        else:
            current_node = self.head

            # find the last node
            while current_node.pointer:
                current_node = current_node.pointer

            current_node.pointer = LinkedNode(value)

    def delete(self, value):
        prev = None
        current_node = self.head

        while current_node:
            if current_node.value == value:
                # delete this
                
                if prev == None:
                    # removing the head
                    self.head = current_node.pointer
                else:
                    prev.pointer = current_node.pointer
                    
                current_node = None
                break
                
            prev = current_node
            current_node = current_node.pointer

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.value, end=", ")
            current_node = current_node.pointer
            
        print("") # newline for formatting

l = LinkedList()
l.insert(5)
l.insert(7)
l.insert(10)
l.insert(12)
l.print_list()
l.delete(5)
l.print_list()
