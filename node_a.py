from node import Node0


class Node1(Node0):
    def __init__(self, item=0, parent=None, left=None, right=None, _dir="left"):
        Node0.__init__(self, item, parent, left, right)
        self.___dir = _dir

    def get__dir(self):
        return self.___dir

    def set__dir(self, item):
        self.___dir = item
