def selectionSort(args):
    for i in range(len(args)):
        min_index = args.index(min(args[i:]))
        if args[i] > min(args[i:]):
            args[i], args[min_index] = args[min_index], args[i]
    print(args)
    return args

selectionSort([5,4,3,2,1])
