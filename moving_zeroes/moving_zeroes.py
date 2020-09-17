'''
Input: a List of integers
Returns: a List of integers
'''
# Move non-zero ints to the left. All zeroes should be on the right

def moving_zeroes(arr):

    for i in range(len(arr)):
        x = arr[i]

        if x != 0:
            # An initial array of "x" and appending slices from arr
            arr = [x] + arr[:i] + arr[i+1:]

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")