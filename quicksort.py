#No iteration, only one processing
def quickSort(arr):
    k=[]
    kr=[]
    kl=[]
    for i in range(len(arr)):
        if i==0:
            k.append(arr[i])
        elif arr[i]>arr[0]:
            kr.append(arr[i])

        elif arr[i]<arr[0]:
            kl.append(arr[i])
    return(kl+k+kr)
