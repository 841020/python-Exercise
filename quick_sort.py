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
        if index != pivot_index:
            continue
        item = lt[index]
        if item >= pivot:
            bigger_lt.append(item)
        elif item < pivot:
            small_lt.append(item)
    full_lt = parser(small_lt) + [pivot]
    full_lt += parser(bigger_lt)
    return full_lt
nums[:] = parser(nums)
