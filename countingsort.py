#Count numbers between 0 and 100
def countingSort(arr):
    x=list(0 for x in range(100))
    for i in arr:
        x[i]=x[i]+1
    return (x)
