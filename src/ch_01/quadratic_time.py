"""
Quadratic Time Complexity (O(n))

Example operations: Nested loops
"""


def get_sum(param: list):
    sum_ = 0
    for row in param:
        for item in row:
            sum_ += item
    return sum_


if __name__ == '__main__':
    values: list = [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9, 11]]
    print(get_sum(values))
