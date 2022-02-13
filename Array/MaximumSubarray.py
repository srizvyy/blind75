arr = [-2,1,-3,4,-1,2,1,-5,4]

def max_sub_arr(nums):
    max_sub = nums[0]
    curr_sum = 0 

    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n 
        max_sub = max(max_sub, curr_sum)
    return max_sub

print(max_sub_arr(arr))