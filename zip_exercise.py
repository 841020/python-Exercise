def foo(args):
  print(args, 'id:', id(args))

a=['1', '2', '3']
b=[4,5,6]
num = zip(a,b)
foo(num)

dt = dict(num)
foo(dt)

lt = list(num)
foo(lt)

tp=tuple(num)
foo(tp)

st=set(num)
foo(st)

print('-------test2----------')
a=['1', '2', '3']
b=[4,5,6]
num = zip(a,b)
foo(num)


lt = list(num)
foo(lt)

tp=tuple(num)
foo(tp)

st=set(num)
foo(st)

dt = dict(num)
foo(dt)
