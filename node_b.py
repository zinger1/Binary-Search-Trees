from node import Node0


class Node2(Node0):
    def __init__(self, item=0, parent=None, left=None, right=None, elem=None):
        Node0.__init__(self, item, parent, left, right)
        self.__elem = elem

    def get__elem(self):
        return self.__elem

    def set__elem(self, address):
        self.__elem = address


class Link:

    def __init__(self, item, _next=None):
        self.__key = item
        self.__next = _next

    def get__next(self):
        return self.__next

    def set__next(self, address):
        self.__next = address

    def get__link_key(self):
        return self.__key

    def set__link_key(self, value):
        self.__key = value
