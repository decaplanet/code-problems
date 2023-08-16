# https://www.algoexpert.io/questions/smallest-difference


# O(n log(n) + m log(m)) time | O(1) space
def smallestDifference(arrayOne: list[int], arrayTwo: list[int]):
    arrayOne.sort()
    arrayTwo.sort()

    current_difference = 0
    smallest_difference = float("inf")
    smallest_pair = []

    index_one = 0
    index_two = 0

    while index_one < len(arrayOne) and index_two < len(arrayTwo):
        element_one = arrayOne[index_one]
        element_two = arrayTwo[index_two]

        if element_one < element_two:
            current_difference = element_two - element_one
            index_one += 1
        elif element_two < element_one:
            current_difference = element_one - element_two
            index_two += 1
        else:
            return [element_one, element_two]

        if current_difference < smallest_difference:
            smallest_difference = current_difference
            smallest_pair = [element_one, element_two]

    return smallest_pair
