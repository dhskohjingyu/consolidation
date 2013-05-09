class BinaryNode():
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

    def get_left(self):
        return self.__left

    def set_left(self, new_left):
        self.__left = new_left

    def get_right(self):
        return self.__right

    def set_right(self, new_right):
        self.__right = new_right

class BinaryTree():
    def __init__(self):
        self.__root = None

    def insert_value(self, value):
        new = BinaryNode(value)
        
        if self.__root == None:
            self.__root = new
        else:
            current_node = self.__root
            inserted = False

            while not inserted:
                if current_node == None:
                    current_node = new
                else:
                    # value less than current_node value
                    if current_node.get_value() < value:
                        if current_node.get_left() == None:
                            current_node.set_left(new)
                            inserted = True
                        else:
                            current_node = current_node.get_left()
                    else:
                        # value more than current_node value
                        if current_node.get_right() ==  None:
                            current_node.set_right(new)
                            inserted = True
                        else:
                            current_node = current_node.get_right()

    def pre_order_print(self):
        self.pre_order(self.__root)

    def pre_order(self, node):
        # root L R
        print(node.get_value())

        if node.get_left() != None:
            self.pre_order(node.get_left())

        if node.get_right() != None:
            self.pre_order(node.get_right())

    def in_order_print(self):
        self.in_order(self.__root)

    def in_order(self, node):
        # L root R
        if node.get_left() != None:
            self.in_order(node.get_left())
            
        print(node.get_value())

        if node.get_right() != None:
            self.in_order(node.get_right())

    def post_order_print(self):
        self.post_order(self.__root)
        
    def post_order(self, node):
        # L R root
        if node.get_left() != None:
            self.post_order(node.get_left())

        if node.get_right() != None:
            self.post_order(node.get_right())
            
        print(node.get_value())

b = BinaryTree()
b.insert_value(4)
b.insert_value(6)
b.insert_value(2)
b.insert_value(5)
print("Pre order print")
b.pre_order_print()
print("In order print")
b.in_order_print()
print("Post order print")
b.post_order_print()
