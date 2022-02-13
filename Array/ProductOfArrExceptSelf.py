arr = [1,2,3,4]

def product_of_arr_except_self(arr):
    res = [1] * (len(arr))

    prefix = 1
    for i in range(len(arr)):
        res[i] = prefix
        prefix = prefix * arr[i]
    postfix = 1
    for i in range(len(arr)-1,-1,-1):
        res[i] *= postfix
        postfix *= arr[i]
    return res 

print(product_of_arr_except_self(arr))