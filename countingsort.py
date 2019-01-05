#Count numbers between 0 and 100
def countingSort(arr):
    x=list(0 for x in range(max(arr)+1))
    a=[]
    for i in arr:
        x[i]=x[i]+1

    for j in range(max(arr)+1):
        if x[j]!=0:
            for k in range(x[j]):
                a.append(j)
        else:
            continue
    return(a)
