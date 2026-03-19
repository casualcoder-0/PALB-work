"""
Experiment: Chocolate Distribution Problem
"""

def findMinDiff(arr, m):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    return min_diff

if __name__ == "__main__":
    arr = [3,4,1,9,56,7,9,12]
    m = 5
    print("Minimum Difference:", findMinDiff(arr, m))
