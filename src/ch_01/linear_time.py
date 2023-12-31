"""
Linear Time Complexity (O(n))

Example operations: Copy, Insert, Delete, Iteration
"""


def get_sum(value: list) -> int | float:
    sum_: int|float = 0
    for item in value:
        sum_ += item
    return sum_


if __name__ == '__main__':
    values: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(get_sum(values))
