"""
Bubble sort is one of the simplest and slowest algorithms used for sorting. It is designed in such a
way that the highest value in a list of data bubbles makes its way to the top as the algorithm loops
through iterations. Bubble sort requires little runtime memory to run because all the ordering
occurs within the original data structure. No new data structures are needed as temporary buffers.
But its worst-case performance is O(N2), which is quadratic time complexity (where N is the
number of elements being sorted). As discussed in the following section, it is recommended to
be used only for smaller datasets. Actual recommended limits for the size of the data for the use
of bubble sort for sorting will depend on the memory and the processing resources available but
keeping the number of elements (N) below 1000 can be considered as a general recommendation.

Bubble sort is based on various iterations, called passes. For a list of size N, bubble sort will have
N-1 passes.
"""

def bubble_sort(test_list: list):
    print(0, test_list)
    last_element_index: int = len(test_list) - 1
    for idx in range(last_element_index):
        if test_list[idx] > test_list[idx + 1]:
            test_list[idx], test_list[idx + 1] = test_list[idx + 1], test_list[idx]
        print(idx + 1, test_list)


def bubble_sort_2(test_list: list):
    print(0, test_list)
    # Exchange the elements to arrange in order
    last_element_index: int = len(test_list) - 1
    for pass_no in range(last_element_index):
        for idx in range(pass_no):
            if test_list[idx] > test_list[idx + 1]:
                test_list[idx], test_list[idx + 1] = test_list[idx + 1], test_list[idx]
    return test_list


def optimized_bubble_sort(test_list: list):
    last_element_index: int = len(test_list) - 1
    for pass_no in range(last_element_index, 0, -1):
        swapped: bool = False
        for idx in range(pass_no):
            if test_list[idx] > test_list[idx + 1]:
                test_list[idx], test_list[idx + 1] = test_list[idx + 1], test_list[idx]
                swapped: bool = True
        if not swapped:
            break
    return test_list


if __name__ == '__main__':
    # list_values: list = [25, 21, 22, 24, 23, 27, 26]

    list_values: list = [25, 21, 22, 24, 23, 20, 26, 23, 25, 27, 26]

    print('\n')
    print('**** Bubble Sort ****')
    print(bubble_sort(list_values))

    print('\n')
    print('**** Bubble Sort 2 ****')
    print(bubble_sort_2(list_values))

    print('\n')
    print('**** Optimized Bubble Sort ****')
    print(optimized_bubble_sort(list_values))
