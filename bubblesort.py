# Move the smallest number to the front
def bubblesort1(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                (a[j], a[j-1]) = (a[j-1], a[j])
            print(a)


b = [10, 9, 8, 7, 6]
bubblesort1(b)
# Move the largest number to the end

print('-----------------')


def bubblesort2(a):
    for i in range(len(a)):
        print(i)
        for j in range(1, len(a)-i):
            if a[j] < a[j-1]:
                (a[j], a[j-1]) = (a[j-1], a[j])
            print(a)


c = [10, 9, 8, 7, 6]
bubblesort2(c)
