# https://www.algoexpert.io/questions/first-duplicate-value


# O(n) time | O(n) space
def firstDuplicateValue(array):
    seen = set()

    for item in array:
        if item in seen:
            return item

        seen.add(item)

    return -1
