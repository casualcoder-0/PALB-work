def smallestSubWithSum(x, arr):
    n = len(arr)
    min_len = n + 1

    for i in range(n):
        curr_sum = arr[i]
        if curr_sum > x:
            return 1

        for j in range(i + 1, n):
            curr_sum += arr[j]
            if curr_sum > x:
                min_len = min(min_len, j - i + 1)

    return 0 if min_len == n + 1 else min_len

if __name__ == "__main__":
    print("Result:", smallestSubWithSum(51, [1,4,45,6,0,19]))
