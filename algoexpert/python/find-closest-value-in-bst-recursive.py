# https://www.algoexpert.io/questions/find-closest-value-in-bst
# Answer from Code Walkthrough

def findClosestValueInBst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, float("inf"))


def find_closest_value_in_bst_helper(tree, target, closest):
    if tree == None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return find_closest_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_value_in_bst_helper(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
