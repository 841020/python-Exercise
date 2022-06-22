# random pivot quick sort (in-place)
import random


def parser(lt):
    if len(lt) < 2:
        return lt
    pivot_index = random.randint(0, len(lt)-1)
    pivot = lt[pivot_index]
    small_lt = list()
    bigger_lt = list()
    for index in range(len(lt)):
        item = lt[index]
        if item >= pivot and index != pivot_index:
            bigger_lt.append(item)
        elif item < pivot and index != pivot_index:
            small_lt.append(item)
    return parser(small_lt) + [pivot] + parser(bigger_lt)


nums = [6, 5, 3, 216, 7, 9]
nums[:] = parser(nums)
