def minmax(arr, k):
    n = len(arr)
    max_values = []
    
    for i in range(n - k + 1):
        max_in_window = max(arr[i:i + k])
        max_values.append(max_in_window)
    
    return min(max_values)

k = int(input("Enter the size of the subarray (k): "))
n = int(input("Enter the number of lanterns (n): "))
arr = [int(input(f"Enter brightness level {i+1}: ")) for i in range(n)]
print("Minimum of maximum brightness levels:", minmax(arr, k))

