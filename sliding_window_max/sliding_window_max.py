'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    iterations = len(nums) - k + 1
    new_set = []

    for current_index in range(iterations):
        this_set = nums[current_index : current_index + k]
        max = this_set[0]
        for m in this_set:
            if m > max:
                max = m
        new_set.append(max)

    return new_set


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
