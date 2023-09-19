# https://www.algoexpert.io/questions/first-duplicate-value


# O(n) time | O(1) space
def firstDuplicateValue(array):
    for item in array:
        abs_item = abs(item)

        if array[abs_item - 1] < 0:
            return abs_item

        array[abs_item - 1] *= -1

    return -1
