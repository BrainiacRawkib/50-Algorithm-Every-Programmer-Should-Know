"""
Merge sort stands distinctively among sorting algorithms, like bubble sort and insertion sort,
for its unique approach. Historically, it’s noteworthy that John von Neumann introduced this
technique in 1940. While many sorting algorithms perform better on partially sorted data, merge
sort remains unfazed; its performance remains consistent irrespective of the initial arrangement
of the data. This resilience makes it the preferred choice for sorting large datasets.
"""


def merge_sort(elements: list):
    if len(elements) <= 1:
        return elements

    # Base condition to break the recursion
    mid = len(elements) // 2  # split the list in half
    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left)  # sort the left half
    merge_sort(right)  # sort the right half

    a, b, c = 0, 0, 0

    # Merge the two halves
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            elements[c] = left[a]
            a += 1
        else:
            elements[c] = right[b]
            b += 1
        c += 1

    # If there are remaining elements in the left half
    while a < len(left):
        elements[c] = left[a]
        a += 1
        c += 1

    # If there are remaining elements in the right half
    while b < len(right):
        elements[c] = right[b]
        b += 1
        c += 1
    return elements


if __name__ == '__main__':
    test_elements = [21, 22, 23, 24, 25, 26, 27]
    print(merge_sort(test_elements))
