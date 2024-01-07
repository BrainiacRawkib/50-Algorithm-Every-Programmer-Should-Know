"""
Swapping variables can be used in Sorting and Searching algorithms
"""

def swap_integers(var_1: int, var_2: int) -> tuple[int, int]:
    var_1, var_2 = var_2, var_1
    return var_1, var_2


if __name__ == '__main__':
    print(swap_integers(1, 2))
    print(swap_integers(10, 20))
    print(swap_integers(11, 22))
    print(swap_integers(110, 220))
