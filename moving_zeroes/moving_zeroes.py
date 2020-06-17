'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeroes = 0
    newarr = []

    for i in arr:
        if i == 0:
            zeroes += 1
        else:
            newarr.append(i)

    for z in range(zeroes):
        newarr.append(0)

    return newarr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")