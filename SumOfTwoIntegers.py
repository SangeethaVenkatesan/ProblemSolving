

# Given 2 integers without + and - (bit manipulation)


if __name__ == '__main__':
    """_summary_
    """
    a = 9
    b = 11

    while (b != 0):
        temp = (a & b) << 1
        a = a ^ b
        # to make sure to use the original value of a and not the new value
        b = temp
    print(a)

    # time complexity O(1)
