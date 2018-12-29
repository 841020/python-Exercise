def insertionSort1(n, arr):
    for i in range(1,n):
        x=arr[i]
        j=i-1
        while j>=0 and arr[j]>x:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=x
        
def insertionSort2(n, arr):
    if n==1: 
        xx(arr)
        print('')
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]: 
                (arr[j],arr[j-1])=(arr[j-1],arr[j])
            else:
                break
