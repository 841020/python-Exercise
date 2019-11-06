from operator import itemgetter


def generate_new_dict(ordered_struct, old_dict):
    '''
        if you want to change all dict's key or 
        only want to get some key-value pairs 
        this function can help
    '''
    new_val = itemgetter(*ordered_struct)(old_dict)
    return dict(zip(ordered_struct, new_val))


dt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
new_key = ('a', 'b', 'c')

new_dt = generate_new_dict(new_key, dt)
# new_dt = {'c': 3, 'a': 1, 'b': 2}
