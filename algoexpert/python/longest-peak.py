# https://www.algoexpert.io/questions/longest-peak


# O(n) time | O(1) space
def longestPeak(array: list[int]):
    longest_peak_length = 0
    index = 1

    while index < len(array) - 1:
        is_peak = array[index -
                        1] < array[index] and array[index + 1] < array[index]

        if not is_peak:
            index += 1
            continue

        left_index = index - 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1

        right_index = index + 2
        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index += 1

        current_peak_length = right_index - left_index - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)

        # index += 1
        index = right_index

    return longest_peak_length
