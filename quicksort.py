# The most important thing about quicksort is Partition.
# quicksort is unstable,Because at the time of Partition,
# the same size as the benchmark can go to either side.
# this is only Partition


def quickSort(arr):
    k = []
    kr = []
    kl = []
    for i in range(len(arr)):
        if i == 0:
            k.append(arr[i])
        elif arr[i] > arr[0]:
            kr.append(arr[i])

        elif arr[i] < arr[0]:
            kl.append(arr[i])
    return(kl+k+kr)
