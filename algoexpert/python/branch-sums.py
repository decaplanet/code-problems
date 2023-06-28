# https://www.algoexpert.io/questions/branch-sums

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root == None:
        return []

    branches = branchSums(root.left) + branchSums(root.right)
    return_list = []

    if branches:
        for item in branches:
            return_list.append(root.value + item)
    else:
        return_list = [root.value]

    return return_list
