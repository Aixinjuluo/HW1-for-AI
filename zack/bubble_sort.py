
def bubble_sort(list):
    if len(list) <= 1:
        return list

    start = 0
    end = len(list)-1

    return sort_list(list, start, end)

def sort_list(list, start, end):
    if end == 0:
        return list

    for i in range(start, end):
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list [i+1]
            list[i+1] = temp

    end -= 1
    sort_list(list, start, end)

    return list

if __name__ == '__main__':
    # creating an empty list
    #lst = []
    lst = [4,9,2,6,7,3,1,5,]

    # number of elements as input
    #n = int(input("Enter number of elements : "))

    # iterating till the range
    #for i in range(0, n):
        #ele = int(input())
        # adding the element
        #lst.append(ele)

    sort_list(lst, 0, 7)

    print(lst)