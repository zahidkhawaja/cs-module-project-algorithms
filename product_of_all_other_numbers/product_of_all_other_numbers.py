'''
Input: a List of integers
Returns: a List of integers
'''
# Product of all numbers except the current index

def product_of_all_other_numbers(arr):
    
    result = []
    rand = 1

    for x in range(0, len(arr)):
        for y in range(0, len(arr)):
            if x == y:
                continue

            rand  = rand * arr[y]

        result.append(rand)
        rand = 1

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
