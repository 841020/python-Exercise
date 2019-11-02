def euclidean(bigger_num, small_num):
    if not bigger_num%small_num:
        print( 'GCD is {}'.format(small_num))
        return
    euclidean(small_num, bigger_num%small_num)
euclidean(7,3)
