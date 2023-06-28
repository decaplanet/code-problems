# https://www.algoexpert.io/questions/find-closest-value-in-bst
# Answer Provided by AlgoExpert

def findClosestValueInBst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, float("inf"))


def find_closest_value_in_bst_helper(tree, target, closest):

    current_node = tree

    while current_node != None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value

        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break

    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
