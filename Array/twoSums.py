arr = [1,5,7,9]
# target = 8

def two_sums(nums, target):
    hash = {}

    for i, num in enumerate(nums):
        diff = target - num 
        if diff in hash:
            return [hash[diff], i]
        hash[num] = i



