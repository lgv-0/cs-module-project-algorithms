'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 0:
        return 0
    elif not n:
        return 1

    baseArr = [1, 2, 4]

    for idkman in range(n):
        if ((idkman + 1) * 3 >= n):
            return baseArr[n - (idkman * 3) - 1]

        next_3 = []
        next_3.append(baseArr[0]+baseArr[1]+baseArr[2])
        next_3.append(next_3[0]+baseArr[1]+baseArr[2])
        next_3.append(next_3[0]+next_3[1]+baseArr[2])
        baseArr = next_3

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 20

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")