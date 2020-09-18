'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Sliding window size "k"
# Moving from left to right
# Max value in each window

def sliding_window_max(nums, k):

    max_nums = []

    if len(nums) >= k:
        for x in range(len(nums) - k + 1):
            window_nums = []
            for y in range(k):
                window_nums.append(nums[x + y])
            max_num = max(window_nums)
            max_nums.append(max_num)

        return max_nums
    else:
        return None


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
