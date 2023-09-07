from bubble_sort import bubble_sort
from merge_sorts import merge_sort, merge
from quick_sort import quick_sort


def hybrid_sort(L, SMALL, BIG, T):

    length = len(L)

    if length < T and SMALL == 1:
        bubble_sort(L)

    if length >= T :
        divide_list(L,SMALL, BIG,T)

    return L


def divide_list(L, SMALL, BIG, T):
    length = len(L)
    mid = int(length/2)
    list_one = L[0:mid]
    list_two = L[mid:length]

    first = hybrid_sort(list_one,SMALL, BIG, T)
    second = hybrid_sort(list_two,SMALL, BIG, T)

    if BIG == 3:
        merge(first, second, L)
    if BIG == 2:
        start = 0
        end = len(L)-1
        quick_sort(L, start, end)


if __name__ == '__main__':
    # creating an empty list
    #lst = []
    L = [4,9,2,6,7,3,1,5,7,11,18,13,12,16,21,3,9,6,13]
    #L = [4, 9, 2, 6, 7, 3, 1,4,6,2,13,2,34,54,62,123,1234,54,2,4,56,5,7,11,17,15,23,2,4,7,12,11,35,2,1]

    # number of elements as input
    #n = int(input("Enter number of elements : "))

    # iterating till the range
    #for i in range(0, n):
        #ele = int(input())
        # adding the element
        #lst.append(ele)

    hybrid_sort(L,1,2,5)

    print(L)