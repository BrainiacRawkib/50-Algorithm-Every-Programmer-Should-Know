"""
As we saw earlier in this chapter, bubble sort is one of the simplest sorting algorithms. Selection
sort is an improvement on bubble sort, where we try to minimize the total number of swaps required
with the algorithm. It is designed to make one swap for each pass, compared to N-1 passes
with the bubble sort algorithm. Instead of bubbling the largest value toward the top in baby
steps (as done in bubble sort, resulting in N-1 swaps), we look for the largest value in each pass
and move it toward the top. So, after the first pass, the largest value will be at the top. After the
second pass, the second largest value will be next to the top value. As the algorithm progresses,
the subsequent values will move to their correct place based on their values.
"""

def selection_sort(elements: list):
    for fill_slot in range(len(elements) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if elements[location] > elements[max_index]:
                max_index = location
        elements[fill_slot], elements[max_index] = elements[max_index], elements[fill_slot]
    return elements


if __name__ == '__main__':
    test_elements: list = [25, 21, 22, 24, 23, 20, 26, 23, 25, 27, 26]
    print(selection_sort(test_elements))
