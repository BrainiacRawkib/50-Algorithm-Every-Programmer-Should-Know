"""
The prerequisite of the binary search algorithm is sorted data. The algorithm iteratively divides
a list into two parts and keeps track of the lowest and highest indices until it finds the value it
is looking for:
"""
from ch_03.sort import bubble_sort


def binary_search(elements: list, item):
    first = 0
    last = len(elements) - 1

    while first <= last:
        mid_point = first + last // 2
        if elements[mid_point] == item:
            return True
        else:
            if item < elements[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return False


if __name__ == '__main__':
    test_elements: list = [12, 33, 11, 99, 22, 55, 90]
    sorted_list = bubble_sort.optimized_bubble_sort(test_elements)
    print(binary_search(sorted_list, 12))
    print(binary_search(sorted_list, 91))
