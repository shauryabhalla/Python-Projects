def merge_sort(arr):
    # If the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Call merge_sort for first half
    left_half = merge_sort(arr[:mid])

    # Call merge_sort for second half
    right_half = merge_sort(arr[mid:])

    # Merge the two halves sorted in step 2 and 3
    return merge(left_half, right_half)

def merge(left, right):
    # A temporary array to store the merged array
    merged = []
    left_index = 0
    right_index = 0

    # Traverse both arrays and insert smaller value from arr1 or arr2
    # into result array and then increment that array index
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are elements left in "left" or "right"
    # append those into the result array
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Test the function
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(f"Sorted array is: {sorted_arr}")
