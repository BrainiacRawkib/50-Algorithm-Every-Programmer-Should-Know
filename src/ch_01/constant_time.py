"""
Constant Time Complexity (O(1))

Example operations: Append, get item, set item
"""

def get_first(value: list[int], index: int) -> int:
    if value:
        try:
            return value[index]
        except IndexError:
            print('Index Error... But returning the first value in the list!')
            return value[0]
    else:
        print('No value in the list...')
        return 0


if __name__ == '__main__':
    values: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(get_first(values, 24))
