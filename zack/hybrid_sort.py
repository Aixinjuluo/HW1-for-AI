from bubble_sort import bubble_sort
from merge_sorts import merge_sort, merge
from quick_sort import quick_sort


#
def hybrid_sort(L, SMALL, BIG, T):
    #get the length of the input list
    length = len(L)
    #check if the list is less than the target number, and if the desired method for sorting, which it's bubble sort
    if length < T and SMALL == 1:
        bubble_sort(L)
    #if the length is freat then the target number, then it will call "deivide_list()"
    #to split the list the half
    if length >= T :
        divide_list(L,SMALL, BIG,T)

    return L

# this is a recursive method
def divide_list(L, SMALL, BIG, T):
    #this is where we split the list to two part
    length = len(L)
    mid = int(length/2)
    list_one = L[0:mid]
    list_two = L[mid:length]
    #we call hybrid_sort() to check the length of the list with the target number for both sublist.
    first = hybrid_sort(list_one,SMALL, BIG, T)
    second = hybrid_sort(list_two,SMALL, BIG, T)

    #if the input number is 3, use mergeSort to merge the sublist together
    if BIG == 3:
        merge(first, second, L)
    # if the input number is 2, use quickSort to merge the sublist together
    if BIG == 2:
        #start pointer is the beginning of the list
        start = 0
        #end pointer is the end of the list
        end = len(L)-1
        #calling quick sort
        quick_sort(L, start, end)


if __name__ == '__main__':
    # creating an empty list
    #lst = []
    L = [4,9,2,6,7,3,1,5,7,11,18,13,12,16,21,3,9,6,13]
    #L = [4, 9, 2, 6, 7, 3, 1,4,6,2,13,2,34,54,62,123,1234,54,2,4,56,5,7,11,17,15,23,2,4,7,12,11,35,2,1]

    hybrid_sort(L,1,2,5)

    print(L)