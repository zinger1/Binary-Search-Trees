from node_b import Node2
from node_b import Link
from tree import Tree


class TreeB(Tree):

    def __init__(self, arr):
        self.count = 0
        self.root = None
        self.__arr = arr
        self.create_tree(arr)

    # update the tree
    def create_tree(self, arr):
        for index in range(len(arr)):
            self.tree_insert(arr[index])

    # insert new node to the tree
    def tree_insert(self, key):
        y = Node2()
        #if the tree is empty
        if self.root is None:
            self.root = Node2(key)
            return
        x = self.root
        #find place for the new node
        while x:
            y = x
            #count tree comparisons
            self.count += 1
            if key < x.get__key():
                x = x.get__left()
            elif key > x.get__key():
                x = x.get__right()
            else:
                self.add_node(key, x)
                return
        new_node = Node2(key)
        new_node.set__parent(y)
        if new_node.get__key() < y.get__key():
            y.set__left(new_node)
        else:
            y.set__right(new_node)
        return

    def add_node(self, key, node):
        new_node = Link(key)
        temp = node.get__elem()
        node.set__elem(new_node)
        new_node.set__next(temp)

    # sort the tree by finding the tree min and his successor
    def sort(self, n):
        new_arr = []
        min_node = self.tree_min(self.root)
        while min_node:
            y = min_node.get__elem()
            new_arr.append(min_node.get__key())
            while y:
                new_arr.append(min_node.get__key())
                y = y.get__next()
            min_node = self.tree_successor(min_node)
        return new_arr


