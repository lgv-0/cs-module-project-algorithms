'''
Input: an integer
Returns: an integer
'''

# 1 - 1
# 2 - 2
# 3 - 4
# 4 - 7
# 5 - 13
# 6 - 24
# 7 - 44
# 8 - 81
# 9 - 149
# 10 - 274

def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0
    elif not n:
        return 1
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")