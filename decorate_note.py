# 沒有參數的 Decorator Function
def decorateApple(f):
    print(2)

    def d_f(*args, **kargs):
        print("apple before call")
        result = f(*args, **kargs)
        print("apple after call")
        return result

    return d_f


@decorateApple
def print_hello():
    print("hello first time.")


print_hello()
print('')

# 沒有參數的 Decorator Class


class decorateAppleClass(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kargs):
        print("apple before call")
        result = self.f(*args, **kargs)
        print("apple after call")
        return result


@decorateAppleClass
def print_hello4():
    print("hello 4th time.")


print_hello4()
print('')
# 有參數的 Decorator Function


def decorateFruit(fruit, rotLevel):
    def outer_d_f(f):
        def d_f(*args, **kargs):
            print("%s %s before call" % (rotLevel, fruit))
            result = f(*args, **kargs)
            print("%s %s after call" % (rotLevel, fruit))
            return result
        return d_f
    return outer_d_f


@decorateFruit('banana', 'new')
def print_hello2():
    print("hello 2nd time.")


print_hello2()
print('')

# 有參數的 Decorator Class


class decorateFruitClass(object):
    def __init__(self, fruit, rotLevel):
        self.fruit = fruit
        self.rotLevel = rotLevel

    def __call__(self, f):
        def d_f(*args, **kargs):
            print("%s %s before call" % (self.rotLevel, self.fruit))
            result = f(*args, **kargs)
            print("%s %s after call" % (self.rotLevel, self.fruit))
            return result
        return d_f


@decorateFruitClass('guava', '80% rot')
def print_hello5():
    print("hello 5th times.")


print_hello5()
print('')
