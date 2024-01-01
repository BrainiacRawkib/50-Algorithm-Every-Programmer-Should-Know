"""
Quadratic Time Complexity (O(n))

Example operations: Finding an element in a sorted array.
"""


def search_binary(list_param: list, item) -> bool:
    first = 0
    last = len(list_param) - 1
    found_flag = False

    while first <= last and not found_flag:
        mid = (first + last) // 2
        if list_param[mid] == item:
            found_flag = True
        else:
            if item < list_param[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found_flag


if __name__ == '__main__':
    print(search_binary([8,9,10,100,1000,2000,3000], 10))
    print(search_binary([8, 9, 10, 100, 1000, 2000, 3000], 5))
