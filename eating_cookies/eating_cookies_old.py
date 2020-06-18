def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0
    elif not n:
        return 1
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)