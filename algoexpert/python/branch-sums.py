# https://www.algoexpert.io/questions/branch-sums
# Referred to a code by "Yegor Yegorov".


def alt_branch_sums(root):
    if root is None:
        return []

    branches = branchSums(root.left) + branchSums(root.right)
    return [x + root.value for x in branches] if branches else [root.value]


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
