'''if your want list/set and dictionary's key get the intersection 
    and make intersection to a new dictionary
'''
from operator import itemgetter

dt = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
new_key = ('a', 'b', 'c')

new_val = itemgetter(*new_key)(dt)
new_dt = dict(zip(new_key, new_val))
# new_dt = {'c': 3, 'a': 1, 'b': 2}
