def b_sort(arr):
    for i in range(len(arr)):
        print(i)
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr
