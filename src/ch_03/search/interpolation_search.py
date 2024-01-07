"""
Binary search is based on the logic that it focuses on the middle section of the data. Interpolation
search is more sophisticated. It uses the target value to estimate the position of the element in
the sorted array. Let’s try to understand it by using an example. Let’s assume we want to search
for a word in an English dictionary, such as the word river. We will use this information to interpolate
and start searching for words starting with r.
"""

def interpolation_search(elements: list, item):
    idx0 = 0
    idxn = len(elements) - 1

    # while idx0 <= idxn and item >= elements[idx0] and item <= elements[idxn]:
    while idx0 <= idxn and elements[idx0] <= item <= elements[idxn]:
        # Find the mid-point
        mid = idx0 + int(((float(idxn - idx0) / (elements[idxn] - elements[idx0])) * (item - elements[idx0])))

        # Compare the value at mid-point with search value
        if elements[mid] == item:
            return True
        if elements[mid] < item:
            idx0 = mid + 1
    return False


if __name__ == '__main__':
    test_elements: list = [12, 33, 11, 99, 22, 55, 90]
    print(interpolation_search(test_elements, 12))
    print(interpolation_search(test_elements, 91))
