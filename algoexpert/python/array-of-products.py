# https://www.algoexpert.io/questions/array-of-products


# O(n) time | O(n) space
def arrayOfProducts(array: list[int]):
    array_length = len(array)
    products = [1] * array_length

    current_left_product = 1
    for i in range(array_length):
        products[i] = current_left_product
        current_left_product *= array[i]

    current_right_product = 1
    for i in reversed(range(array_length)):
        products[i] *= current_right_product
        current_right_product *= array[i]

    return products
