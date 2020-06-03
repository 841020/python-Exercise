import sqlite3
import pickle
from functools import wraps
import xml.etree.ElementTree as ET
from functools import total_ordering
import random
import sys
import urllib.request

# 第三章練習
# 3.1

str1 = sys.argv[1:]
print('有{}個不重複字串:{}'.format(len(set(str1)), set(str1)))
# 3.2
str2 = sys.argv[1]
str3 = sys.argv[2:]
print('{} 出現了{}次'.format(str2, str3.count(str2)))

# 第四章練習
# 4.1
# armstrong number
armstrong_num = []
for i in range(100, 1000):
    a = str(i)
    if int(a[0])**3 + int(a[1])**3 + int(a[2])**3 == i:
        armstrong_num.append(i)
print(armstrong_num)
# 4.2
# 費波那係數


def fn(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        print(c, end=' ')
        c = a+b
        a, b = c, a


n = input()
fn(int(n))
# 費波那係數 推算


def fn(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fn(n-1) + fn(n-2)


n = input()
print(fn(int(n)))
# 4.3
# 撲克牌洗牌
color = {'桃', '心', '梅', '磚'}
number = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
poke = {i+j for i in color for j in number}
print(poke)
# 4.4
a = [(i, j, k) for i in range(1, 11) for j in range(1, 11)
     for k in range(1, 11) if (i**2)+(j**2) == k**2 and (i+j+k) == 24]
print(a)

# 第六章
# 6.1

num = str(random.randint(0, 9))
n = input('guess a number')
while n != num:
    n = input('guess a number')
print('猜中了')

# 6.2
# Implement rich comparison


@total_ordering
class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        self.numer = numer
        self.denom = denom

    def __add__(self, that):
        return Rational(
            self.numer * that.denom + that.numer * self.denom,
            self.denom * that.denom
        )

    def __sub__(self, that):
        return Rational(
            self.numer * that.denom - that.numer * self.denom,
            self.denom * that.denom
        )

    def __mul__(self, that):
        return Rational(
            self.numer * that.numer,
            self.denom * that.denom
        )

    def __truediv__(self, that):
        return Rational(
            self.numer * that.denom,
            self.denom * that.numer
        )

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __repr__(self):
        return f'Rational({self.numer}, {self.denom})'

    def __eq__(self, that):
        return self.numer/self.denom == that.numer/that.denom

    def __gt__(self, that):
        return self.numer/self.denom > that.numer/that.denom


s1 = Rational(2, 5)
s2 = Rational(1, 5)

print(s1 > s2)
print(s1 >= s2)
print(s2 < s1)
print(s2 <= s1)
print(s1 == s2)
print(s1 != s2)

# 第七章練習

# 7.1
# customize exception


class BankException(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalMoneyException(BankException):
    def __init__(self, message):
        super().__init__(message)


class InsufficientException(BankException):
    def __init__(self, message):
        super().__init__(message)


class Account:
    def __init__(self, name: str, number: str, balance: float) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    def amount_check(self, amount: float):
        if amount <= 0:
            raise IllegalMoneyException(f'存款金額不得為負{amount}')

    def deposit(self, amount: float):
        self.amount_check(amount)
        self.balance += amount

    def withdraw(self, amount: float):
        self.amount_check(amount)
        if amount > self.balance:
            raise InsufficientException(f'餘額不足{amount}')
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account('{self.name}', '{self.number}', {self.balance})"


a = Account('mike', '123', 1000)
a.withdraw(2000)
a.withdraw(-2000)
a.deposit(-100)

# 7.2
# Implement context manager


class Suppress:
    def __init__(self, ex_type):
        self.ex_type = ex_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is self.ex_type:
            return True
        return False


with Suppress(ZeroDivisionError):
    a = 9/0
# 7.3實作contextmanager


class _GeneratorContextManager:
    def __init__(self, func, args, kwds):
        self.gen = func(*args, **kwds)
        self.func, self.args, self.kwds = func, args, kwds

    def __enter__(self):

        try:
            return next(self.gen)
        except StopIteration:
            raise RuntimeError("generator didn't yield") from None

    def __exit__(self, type, value, traceback):
        if type is None:
            try:
                next(self.gen)
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")
        else:
            if value is None:

                value = type()
            try:
                self.gen.throw(type, value, traceback)
            except StopIteration as exc:

                return exc is not value
            except RuntimeError as exc:

                if exc is value:
                    return False

                if type is StopIteration and exc.__cause__ is value:
                    return False
                raise
            except:

                if sys.exc_info()[1] is value:
                    return False
                raise
            raise RuntimeError("generator didn't stop after throw()")


def contextmanager(func):
    @wraps(func)
    def helper(*args, **kwds):
        return _GeneratorContextManager(func, args, kwds)
    return helper


def suppress(ex_type):
    try:
        yield
    except ex_type:
        pass


suppress = contextmanager(suppress)
with suppress(ZeroDivisionError):
    9/0


class Some:
    def __init__(self, name):
        self.name = name

    def close(self):
        print(self.name, 'is closed')


def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


closing = contextmanager(closing)
with closing(Some('Resource')) as res:
    print(res.name)
# 第八章練習
# 8.1


def dump(in_f, out_f):
    with in_f as input_f, out_f as output:
        output.write(input_f.read())
# 8.2


def dump(in_f, out_f):
    with in_f as input_f, out_f as output:
        try:
            raise ValueError('fuck you')
            output.write(input_f.read())
        except Exception as f:
            import traceback
            traceback.print_exc(file=open('exception.log', 'w+'))
# 8.3


def xx(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w', encoding='utf8') as output:
        output.write(input_f.read())
# 第九章練習
# 9.1


class MultiMap:
    def __init__(self, dt_1, dt_2):
        self.dt = dict()
        for key, value in dt_1.items():
            self.__insert__(key, value)
        for key, value in dt_2.items():
            self.__insert__(key, value)

    def __repr__(self):
        return '{}'.format(self.dt)

    def __setitem__(self, key, value):
        self.__insert__(key, value)

    def __insert__(self, key, value):
        b = self.dt.get(key)
        if not b:
            self.dt[key] = {value}
        else:
            b.add(value)


b = MultiMap({'a': 2}, {'b': 3, 'a': 5})
print(b)
b['a'] = 6
print(b)

# 9.2
words = ['RADAR', 'WARTER START', 'MILK KLIM', 'RESERVERED', 'IWI', 'ABBA']
output = []
for c in words:
    if c == c[::-1]:
        output.append(c)

# 第十章
# 10.1

with sqlite3.connect('db.sqlite3') as conn:
    conn.cursor().execute('''create table message (id integer primary key autoincrement unique not null,
            title text not null, instance text not null)''')
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


class DVD:
    def __init__(self, title: str, year: int, duration: int, director: str) -> None:
        self.title = title
        self.year = year
        self.duration = duration
        self.director = director

    def save(self):
        cursor.execute('insert into message (title, instance) values (?,?)',
                       (self.title,
                        pickle.dumps(self)))
        conn.commit

    @ staticmethod
    def load(filename: str) -> 'DVD':
        cursor.execute(
            'select instance from message where title = ?', (filename,))
        a = cursor.fetchone()
        return pickle.loads(a[0])

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "DVD('{0}', {1}, {2}, '{3}')".format(
            self.title, self.year, self.duration, self.director)


dvd1 = DVD('Birds', 2018, 8, 'Justin Lin')
dvd1.save()
dvd2 = DVD.load('Birds')
print(dvd2)
# 10.2


def dict_to_xml(root, kwargs):
    user = ET.Element(root)
    for key, value in kwargs.items():
        key = ET.Element(key)
        key.text = str(value)
        user.append(key)
    return ET.tostring(user).decode()


dict_to_xml('user', {'age': 40, 'name': 'Justin'})
