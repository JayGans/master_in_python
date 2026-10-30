def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]


    result = quick_sort(left) + [pivot] + quick_sort(right)
    #print("fun return - ", result)
    return result

arr = [5,3,8,1,2]

print(quick_sort(arr))