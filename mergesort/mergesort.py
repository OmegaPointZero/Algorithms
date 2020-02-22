unsorted_list = [27, 369, 63, 126, 252, 990, 54, 18]

def merge_sort(unsorted):
    if len(unsorted) > 1:
        mid = len(unsorted)//2
        left = merge_sort(unsorted[:mid])
        right = merge_sort(unsorted[mid:])  
        result = merge(left, right)
        return result
    else:
        return unsorted

def merge(left, right):
    sorted_list = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    while len(left) > 0:
        sorted_list.append(left.pop(0))
    while len(right) > 0:
        sorted_list.append(right.pop(0))
    return sorted_list
    
print merge_sort(unsorted_list)
