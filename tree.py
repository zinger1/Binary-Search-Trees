from node import Node0


class Tree:

    def __init__(self, arr):
        self.count = 0
        self.root = None
        self.__arr = arr
        self.create_tree(arr)

    # update the regular tree
    def create_tree(self, arr):
        for index in range(len(arr)):
            new_node = Node0(arr[index])
            self.tree_insert(new_node)

    #insert new node to the tree
    def tree_insert(self, new_node):
        y = None
        #if the tree is empty
        if self.root is None:
            self.root = new_node
            return
        x = self.root
        #find place for the new node
        while x:
            y = x
            #count tree comparisons
            self.count += 1
            if new_node.get__key() < x.get__key():
                x = x.get__left()
            else:
                x = x.get__right()

        new_node.set__parent(y)
        if y is None:
            self.root = new_node
            return
        if new_node.get__key() < y.get__key():
            y.set__left(new_node)
        else:
            y.set__right(new_node)
        return

#sort the tree by finding the tree min and his successor

    def sort(self, n):
        new_arr = []
        min_node = self.tree_min(self.root)
        while min_node:
            new_arr.append(min_node.get__key())
            min_node = self.tree_successor(min_node)
        return new_arr

#find the minimal node(x) in the tree
    def tree_min(self, x):
        while x.get__left():
            x = x.get__left()
        return x
#find the successor of the current node(node)
    def tree_successor(self, node):
        if node.get__right():
            return self.tree_min(node.get__right())
        parent_node = node.get__parent()
        while parent_node and node is parent_node.get__right():
            node = parent_node
            parent_node = parent_node.get__parent()
        return parent_node

