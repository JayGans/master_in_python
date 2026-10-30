def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

    print(arr)

arr = [6,5,2,3,1,9,8]
sort(arr)                