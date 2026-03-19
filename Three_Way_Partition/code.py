def threeWayPartition(arr, a, b):
    start, end = 0, len(arr)-1
    i = 0

    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1

    return arr

if __name__ == "__main__":
    print(threeWayPartition([1,4,3,6,2,1], 1, 3))
