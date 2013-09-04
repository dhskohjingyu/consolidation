class BST(object):
    ''' binary search tree class '''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            # insert to right
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            # insert to left
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)

    def lookup(self, value, parent=None):
        if self.value == value:
            return self, parent
        else:
            if value > self.value:
                # node is on the right subtree
                if self.right != None:
                    return self.right.lookup(value, self)
                else:
                    return None
            else:
                # node is on left subtree
                if self.left != None:
                    return self.left.lookup(value, self)
                else:
                    return None
    def get_smallest(self):
        ''' returns the child with the largest value '''
        if self.left == None:
            return self
        else:
            return self.left.get_smallest()

    def get_largest(self):
        ''' returns the child with the largest value '''
        if self.right == None:
            return self
        else:
            return self.right.get_largest()

    def remove(self, value):
        ''' removes a node from this tree '''
        node_to_remove, parent = self.lookup(value)

        # no children, just remove
        if node_to_remove.left == None and node_to_remove.right == None:
            if parent.left == node_to_remove:
                parent.left = None
            elif parent.right == node_to_remove:
                parent.right = None
        # two subtrees
        elif node_to_remove.left != None and node_to_remove.right != None:
            # replace with smallest node on right subtree
            successor = node_to_remove.right.get_smallest()
            successor.left = node_to_remove.left
            successor.right = None

            if parent.left == node_to_remove:
                parent.left = successor
            elif parent.right == node_to_remove:
                parent.right = successor
        else:
            # one subtree
            successor = None

            if node_to_remove.left:
                successor = node_to_remove.left
            elif node_to_remove.right:
                successor = node_to_remove.right

            if parent.left == node_to_remove:
                parent.left = successor
            elif parent.right == node_to_remove:
                parent.right = successor

    def in_order(self):
        # L Root R
        if self.left != None:
            self.left.in_order()

        print(self.value, end=", ")

        if self.right != None:
            self.right.in_order()
            
if __name__ == "__main__":
    b = BST(9)
    b.insert(10)
    b.insert(5)
    b.insert(7)
    b.insert(3)
    b.in_order()

    print("removing 5")
    b.remove(5)

    b.in_order()
