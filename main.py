arr = [1,3,5,6]
target = [8]
def two_sum(arr, target):
    values = dict()
    
    for i, elum in enumerate(arr):
        comp = target - elum
        
        if comp in values:
            
            return [values[comp], i]

        values[elum] = i 
    return []

list1 = two_sum(arr, target)
print(list1)