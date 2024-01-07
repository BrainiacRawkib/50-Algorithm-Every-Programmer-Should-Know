"""
One of the simplest strategies for searching data is to simply loop through each element looking
for the target. Each data point is searched for a match and, when a match is found, the results are
returned and the algorithm exits the loop. Otherwise, the algorithm keeps on searching until it
reaches the end of the data. The obvious disadvantage of linear search is that it is very slow due
to the inherent exhaustive search. The advantage is that the data does not need to be sorted, as
required by the other algorithms presented in this chapter.
"""


def linear_search(elements: list, item):
    index = 0
    found = False

    # Match the value with each data element
    while index < len(elements) and found is False:
        if elements[index] == item:
            found = True
        else:
            index += 1
    return found


if __name__ == '__main__':
    test_elements = [12, 33, 11, 99, 22, 55, 90]
    print(linear_search(test_elements, 12))
    print(linear_search(test_elements, 91))
