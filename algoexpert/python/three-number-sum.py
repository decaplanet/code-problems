# https://www.algoexpert.io/questions/three-number-sum


# O(n^2) time | O(n) space
def threeNumberSum(array: list[int], targetSum: int):
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        index_left = i + 1
        index_right = len(array) - 1

        while index_left < index_right:
            current_sum = array[i] + array[index_left] + array[index_right]

            if current_sum == targetSum:
                triplets.append(
                    [array[i], array[index_left], array[index_right]])
                index_left += 1
                index_right -= 1
            elif current_sum < targetSum:
                index_left += 1
            elif current_sum > targetSum:
                index_right -= 1

    return triplets
