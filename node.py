class Node0:

    def __init__(self, key=0, parent=None, left=None, right=None):
        self.__key = key
        self.__parent = parent
        self.__left = left
        self.__right = right

    def get__key(self):
        return self.__key

    def set__key(self, value):
        self.__key = value

    def get__parent(self):
        return self.__parent

    def set__parent(self, address):
        self.__parent = address

    def get__left(self):
        return self.__left

    def set__left(self, address):
        self.__left = address

    def get__right(self):
        return self.__right

    def set__right(self, address):
        self.__right = address


