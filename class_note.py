class foo:
    def bar(self):
        print(123)
#直接呼叫類別裡面的方法
foo().bar()

#建立實例，呼叫類別裡面的方法
a=foo
a().bar()

b=foo()
b.bar()

#靜態方法(未建立實例)
foo.bar(a)

#在實例中增加類別屬性
class foo1:
    pass

b=foo1
b.num=123
foo1.num
dir(foo1)
foo1.__dict__

c=foo1()
c.num=123
foo1.num

dir(foo1)
foo1.__dict__

#子類呼叫父類的方法
class foo2:
    def bar(self):
        print(123)

class foo3(foo2):
    def xx(self):
        foo2.bar(self)

foo3().xx()
