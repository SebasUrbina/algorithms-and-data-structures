"""
Implementación del algoritmo binary search de python
"""

"""

[5,1,3,2,5]

[LEFT,...,MID,...,RIGHT]

MID = (LEFT) + (RIGHT-LEFT)//2


"""


def binarySearch(array: list[int], target: int):
    """Binary search algorithm"""

    array.sort()

    left, right = 0, len(array) - 1

    while left <= right:
        
        mid = left + (right-left)//2

        # Si el target esta justo al medio. Check
        if array[mid] == target:
            return mid
        
        # Si el target está a la izquierda
        elif array[mid] <= target:
            left = mid + 1

        # Si el target está a la derecha
        else:
            right = mid - 1
        
    return -1

# Testing
# [1,2,3,5,6]
assert binarySearch([3,1,2,5,6], 6) == 4


