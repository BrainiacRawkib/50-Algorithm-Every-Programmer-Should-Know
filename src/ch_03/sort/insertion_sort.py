"""
The basic idea of insertion sort is that in each iteration, we remove a data point from the data
structure we have and then insert it into its right position. That is why we call this the insertion
sort algorithm.

Use cases and recommendations
Insertion sort is exceptionally efficient for:
• Small datasets.
• Nearly sorted datasets, where only a few elements are out of order.
"""


def insertion_sort(elements: list):
    for i in range(1, len(elements)):
        j = i - 1
        next_element = elements[i]

        # Iterate backward through the sorted portion,
        # Looking for the appropriate position for `next_element`
        while j >= 0 and elements[j] > next_element:
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = next_element
    return elements


if __name__ == '__main__':
    test_elements: list[int] = [25, 21, 22, 24, 23, 27, 26]
    print(insertion_sort(test_elements))
