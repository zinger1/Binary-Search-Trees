from node_a import Node1
from tree import Tree


class TreeA(Tree):
    # update the tree
    def create_tree(self, arr):
        for index in arr:
            new_node = Node1(index)
            self.tree_insert(new_node)



    # insert new node to the tree
    def tree_insert(self, new_node):
        y = None
        #if the tree is empty
        x = self.root
        #find place for the new node
        son = "left"
        while x:
            y = x
            #count tree comparisons
            self.count += 1
            if new_node.get__key() < x.get__key():
                x = x.get__left()
            elif new_node.get__key() > x.get__key():
                x = x.get__right()
            else:
                #update the dir field
                if x.get__dir() == "left":
                    x.set__dir("right")
                    x = x.get__left()
                    son = "left"
                else:
                    x.set__dir("left")
                    x = x.get__right()
                    son = "right"
        new_node.set__parent(y)
        if y is None:
            self.root = new_node
            return
        if new_node.get__key() < y.get__key():
            y.set__left(new_node)
        elif new_node.get__key() > y.get__key():
            y.set__right(new_node)
        elif son == "right":
            y.set__right(new_node)
        else:
            y.set__left(new_node)


