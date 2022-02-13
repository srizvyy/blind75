arr1 = [1,2,3,4,1]
arr2 = [1,2,3,4,5]

def contains_dublicate(arr):
    hashset = set()

    for num in arr:
        if num in hashset:
            return True 
        hashset.add(num)

print(contains_dublicate(arr1))