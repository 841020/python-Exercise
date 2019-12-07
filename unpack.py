#args & kwargs test
def foo(*args):
    print(args, 'id:', id(args))

foo(1,2,3,4,5)
num = range(1,6)
print('id:', id(num))
foo(*num)
foo(*list(num))
foo(*tuple(num))
foo(*set(num))
foo(*zip(num, range(5)))

dt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('id:', id(dt))
foo(*dt.items())
foo(*dt.keys())
foo(*dt.values())

def bar(**kwargs):
    print(kwargs, 'id:', id(kwargs))

bar(a=1, b=2, c=3, d=4, e=5)
bar(**dt)
bar(**dict(a=1, b=2, c=3, d=4, e=5))

a=['1', '2', '3']
b=[4,5,6]
num = zip(a,b)
dt = dict(num)
print(dt, id(dt))
bar(**dt)
