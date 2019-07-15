# Move the smallest number to the front
def bubblesort1(a):
    counter = 0
    for i in range(len(a)-1):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                (a[j], a[j-1]) = (a[j-1], a[j])
                counter += 1
   
    print('Array is sorted in '+str(counter)+' swaps.')
    print('First Element: '+str(a[0]))
    print('Last Element: '+str(a[-1]))

# Move the largest number to the end


def bubblesort2(a):
    counter = 0
    for i in range(len(a)-1):
        for j in range(1, len(a)-i):
            if a[j] < a[j-1]:
                (a[j], a[j-1]) = (a[j-1], a[j])
                counter += 1
          
    print('Array is sorted in '+str(counter)+' swaps.')
    print('First Element: '+str(a[0]))
    print('Last Element: '+str(a[-1]))
