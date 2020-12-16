from tree import Tree
from tree_a import TreeA
from tree_b import TreeB
from tree_c import TreeC
from menu import *

arr, n = menu()
tree = Tree(arr)
tree1 = TreeA(arr)
tree2 = TreeB(arr)
tree3 = TreeC(arr)
new_arr = tree.sort(n)
new_arr1 = tree1.sort(n)
new_arr2 = tree2.sort(n)
new_arr3 = tree3.sort(n)
result(new_arr, new_arr1, new_arr2, new_arr3, tree.count, tree1.count, tree2.count, tree3.count)
