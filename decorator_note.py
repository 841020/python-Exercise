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
# Python 中的函数
def hi(name="yasoob"):
    return "hi " + name
print(hi)
# 
    
print(hi())
# output: 'hi yasoob'
 
# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个
 
print(greet())
# output: 'hi yasoob'
 
# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
print(hi())
#outputs: NameError
 
print(greet())
#outputs: 'hi yasoob'

#在函数中定义函数<首先要清楚函數中的韓式的執行順序

def hi(name="yasoob"):
    print("now you are inside the hi() function")
 
    def greet():
        print(1)
        return "now you are in the greet() function"
 
    def welcome():
        print(2)
        return "now you are in the welcome() function"
    print(greet())
    print(welcome())
    print("now you are back in the hi() function")
    
hi()
#output:now you are inside the hi() function
#       1
#       now you are in the greet() function
#       2
#       now you are in the welcome() function
#       now you are back in the hi() function

# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：
 
greet()
#outputs: NameError: name 'greet' is not defined

def add_one(number):
    return number + 1

add_one(2) # 輸出3
#上面的例子是參數傳遞進函數中一個基本例子

#从函数中返回函数
#其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：


def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
 
    def welcome():
        return "now you are in the welcome() function"
 
    if name == "yasoob":
        return greet
    else:
        return welcome
 
a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>
 
#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
#现在试试这个
 
print(a())
#outputs: now you are in the greet() function
#再次看看这个代码。在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。
#为什么那样？这是因为当你把一对小括号放在后面，
#这个函数就会执行；然而如果你不放括号在它后面，
#那它可以被到处传递，并且可以赋值给别的变量而不去执行它。 

#当我们写下 a = hi()，hi() 会被执行，而由于 name 参数默认是 yasoob，
#所以函数 greet 被返回了。如果我们把语句改为 a = hi(name = "ali")，
#那么 welcome 函数将被返回。我们还可以打印出 hi()()，
#这会输出 now you are in the greet() function。



#在python中我們知道，參數可以傳遞進函數，可是你知道函數也可以當參數傳遞嗎？
#聽起來有點饒口，這句話的意思是函數也可以當成參數傳進其他的函數
#以下是一個例子

def greet_bob(greeter_func):
    return greeter_func()

def say_hello():
    return "Hello"

greet_bob(say_hello) #輸出 'Hello'

#如果是使用decorator的話會變成
@greet_bob
def say_hello():
   return f"Hello"

say_hello()   #輸出'Hello'

#以上的例子我們可以得到一個結論
say_hello = greet_boB(say_hello)
#在裝飾器包裝下 執行say_hello() 如同執行greet_boB(say_hello)


#待補介紹
#function()
#*args
#**kwargs
#函數無參數裝飾器無參數
#函數有參數裝飾器無參數
#函數無參數裝飾器有參數
#函數有參數裝飾器有參數
#class 的裝飾器寫法


#參考
#http://www.runoob.com/w3cnote/python-func-decorators.html
