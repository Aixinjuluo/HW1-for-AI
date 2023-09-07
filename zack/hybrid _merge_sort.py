
# Press the green button in the gutter to run the script.

def merge(left_side, right_side, merge_list):
    left = int(len(merge_list) / 2)
    right = len(merge_list) - left

    i = 0
    l = 0
    r = 0

    while l < left and r < right:
        if left_side[l] > right_side[r]:
            merge_list[i] = right_side[r]
            i += 1
            r += 1
        else:
            merge_list[i] = left_side[l]
            i += 1
            l += 1
    while l < left:
        merge_list[i] = left_side[l]
        i += 1
        l += 1
    while r < right:
        merge_list[i] = right_side[r]
        i += 1
        r += 1


def merge_sort(list):
    length = len(list)

    # base case
    if length <= 1:
        return list

    middle = int(length / 2)
    left_list = [0]*middle
    right_list = [0]*(length - middle)
    left_index = 0
    right_index = 0

    for i in range(length):
        if i < middle:
            left_list[left_index] = list[i]
            #i += 1
            left_index += 1
        else:
            right_list[right_index] = list[i]
            #i += 1
            right_index += 1

    merge_sort(left_list)
    merge_sort(right_list)
    merge(left_list, right_list, list)


if __name__ == '__main__':
    # creating an empty list
    #lst = []
    lst = [4,3,2,5,7,3,98,2,3,67,24,9,100,1]

    # number of elements as input
    #n = int(input("Enter number of elements : "))

    # iterating till the range
    #for i in range(0, n):
        #ele = int(input())
        # adding the element
        #lst.append(ele)

    merge_sort(lst)

    print(lst)
