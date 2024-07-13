lst = [7,15,6,8,15,90,90,56,100]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key

# Test the function
lst = [7,15,6,8,15,90,90,56,100]
insertion_sort(lst)
print(lst)