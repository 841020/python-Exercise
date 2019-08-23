#args &kwargs test
def foo(*args):
    print(args)

def bar(**kwargs):
    print(kwargs)

foo(1, 2, 3, 4, 5)
foo(1,2,3,4,5)
foo(*[1,2,3,4,5])
foo(*(1,2,3,4,5))
foo(*{1,2,3,4,5})
a=[1,2,3,4]
foo(*a)
a={1,2,3,4}
foo(*a)
a=(1,2,3,4)
foo(*a)

bar(a=1, b=2, c=3, d=4, e=5)
bar(**{'1':2,'2':3})
b={'1':2,'2':3}
bar(**b)

def foo2(c,b,a):
    print('a',a)
    print('b',b)
    print('c',c)
c={'a':1,'b':2,'c':3}
foo2(**c)
def foo3(a,b,c):
    print('a',a)
    print('b',b)
    print('c',c)
c={'b':2,'c':3,'a':1}
foo3(**c)
