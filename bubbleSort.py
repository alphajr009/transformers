def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(unsorted_array)
print("Sorted array:", unsorted_array)
