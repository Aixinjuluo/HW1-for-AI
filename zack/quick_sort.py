
def partition(new_list, start, end):

    pivot = new_list[end]
    i = start-1

    for j in range(start, end):
        if new_list[j] < pivot:
            i += 1
            temp = new_list[j]
            new_list[j] = new_list[i]
            new_list[i] = temp
    i += 1
    temp = new_list[i]
    new_list[i] = new_list[end]
    new_list[end] = temp

    return i

def quick_sort(list, start, end):
    if end <= start:
        return list
    else:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot-1)
        quick_sort(list, pivot +1, end)


if __name__ == '__main__':
    # creating an empty list
    #lst = []
    lst = [4,9,2,6,7,3,1,5]

    # number of elements as input
    #n = int(input("Enter number of elements : "))

    # iterating till the range
    #for i in range(0, n):
        #ele = int(input())
        # adding the element
        #lst.append(ele)

    quick_sort(lst, 0, 7)

    print(lst)