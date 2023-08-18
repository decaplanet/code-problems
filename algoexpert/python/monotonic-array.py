# https://www.algoexpert.io/questions/monotonic-array


# O(n) time | O(1) space
def isMonotonic(array: list[int]):
    non_decreasing = True
    non_increasing = True

    if len(array) < 2:
        return True

    if len(array) > 1:
        for i in range(1, len(array)):
            if non_decreasing != False:
                if array[i] >= array[i - 1]:
                    non_decreasing = True
                else:
                    non_decreasing = False

            if non_increasing != False:
                if array[i] <= array[i - 1]:
                    non_increasing = True
                else:
                    non_increasing = False

        return non_decreasing or non_increasing
