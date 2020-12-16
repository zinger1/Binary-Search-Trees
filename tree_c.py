from node import Node0
from tree import Tree
import random


class TreeC(Tree):
    # insert new node to the tree
    def tree_insert(self, new_node):
        y = None
        if self.root is None:
            self.root = new_node
            return
        x = self.root
        while x:
            #count tree comparisons
            self.count += 1
            y = x
            if new_node.get__key() < x.get__key():
                x = x.get__left()
            elif new_node.get__key() > x.get__key():
                x = x.get__right()
            else:
                #update the direct variable by random function
                direct = random.choice([1, 0])
                if direct == 0:
                    x = x.get__left()
                else:
                    x = x.get__right()
        new_node.set__parent(y)
        if new_node.get__key() < y.get__key():
            y.set__left(new_node)
        elif new_node.get__key() > y.get__key():
            y.set__right(new_node)
        elif direct == 0:
            y.set__left(new_node)
        else:
            y.set__right(new_node)
        return
