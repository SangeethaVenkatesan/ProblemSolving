# Rule : Use HashMap


# Ouput, exactly one soln
# nums[0]= 2 and nums[1] = 7 return [0,1]


def twoSum(nums, target):
    # Trick to use HashMap
    prev_map = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], index]
        else:
            prev_map[num] = index
    return


if __name__ == '__main__':
    # Given
    nums = [2, 7, 11, 15]
    target = 9

    result = twoSum(nums, target)
    print(result)

# Time complexity
# O(n) for linear pass and Space complexity - O(n) {for extra memory}
