def bubblesort(a):
    b=sorted(a)
    if a==b:
        print('Array is sorted in 0 swaps.')
        print('First Element: '+str(a[0]))
        print('Last Element: '+str(a[-1]))
    else:
        counter=0
        while a!=b:
            for i in range(1,len(a)):
                if a[i]<a[i-1]:
                    (a[i],a[i-1])=(a[i-1],a[i])
                    counter+=1
                elif a==b:
                    break
        print('Array is sorted in '+str(counter)+' swaps.')
        print('First Element: '+str(a[0]))
        print('Last Element: '+str(a[-1]))
