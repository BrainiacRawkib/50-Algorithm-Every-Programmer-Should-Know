"""
The bubble sort algorithm compares immediate neighbors and exchanges them if they are out of
order. On the other hand, insertion sort creates the sorted list by transferring one element at a
time. If we have a partially sorted list, insertion sort should give reasonable performance.

But for a totally unsorted list, sized N, you can argue that bubble sort will have to fully iterate
through N-1 passes in order to get it fully sorted.

Now, let’s understand this concept.

In pass one, instead of selecting immediate neighbors, we use elements that are at a fixed gap,
eventually sorting a sublist consisting of a pair of data points. This is shown in the following
diagram. In pass two, it sorts sublists containing four data points (see the following diagram).
In subsequent passes, the number of data points per sublist keeps on increasing and the number
of sublists keeps on decreasing until we reach a situation where there is just one sublist that
consists of all the data points.
"""

def shell_sort(elements: list):
    distance = len(elements) // 2

    while distance > 0:
        for i in range(distance, len(elements)):
            temp = elements[i]
            j = i

            # Sort the sub list for this distance
            while j >= distance and elements[j - distance] > temp:
                elements[j] = elements[j - distance]
                j = j - distance
            elements[j] = temp

        # Reduce the distance for the next element
        distance = distance // 2
    return elements


if __name__ == '__main__':
    test_elements: list = [25, 21, 22, 24, 23, 20, 26, 23, 25, 27, 26]
    print(shell_sort(test_elements))
