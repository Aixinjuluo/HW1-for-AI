# Define a function 'partition' that takes a list 'new_list', a start index 'start', and an end index 'end'.
def partition(new_list, start, end):
    # Select the pivot element as the last element of the list.
    pivot = new_list[end]
    i = start - 1  # Initialize the index 'i' to start-1.

    # Iterate through the elements from 'start' to 'end-1'.
    for j in range(start, end):
        # If the current element is less than the pivot, swap it with the element at index 'i+1'.
        if new_list[j] < pivot:
            i += 1
            temp = new_list[j]
            new_list[j] = new_list[i]
            new_list[i] = temp

    # Swap the pivot element with the element at index 'i+1'.
    i += 1
    temp = new_list[i]
    new_list[i] = new_list[end]
    new_list[end] = temp

    # Return the index 'i' where the pivot element is now positioned.
    return i

# Define a recursive function 'quick_sort' that sorts a list 'list' from index 'start' to 'end'.
def quick_sort(list, start, end):
    if end <= start:
        return list  # If the sublist has only one or zero elements, it's already sorted.

    # Partition the list and get the index of the pivot element.
    pivot = partition(list, start, end)

    # Recursively sort the two sublists to the left and right of the pivot.
    quick_sort(list, start, pivot - 1)
    quick_sort(list, pivot + 1, end)

if __name__ == '__main__':
    # Create an example list 'lst'.
    lst = [4, 9, 2, 6, 7, 3, 1, 5]

    # Call 'quick_sort' to sort the list 'lst' from index 0 to 7.
    quick_sort(lst, 0, 7)

    # Print the sorted list.
    print(lst)