#第三章練習
#1
import sys
str1 = sys.argv[1:]
print('有{}個不重複字串:{}'.format(len(set(str1)), set(str1)))
#2
str2 = sys.argv[1]
str3 = sys.argv[2:]
print('{} 出現了{}次'.format(str2, str3.count(str2)))

#第四章練習
# armstrong number
armstrong_num = []
for i in range(100,1000):
    a=str(i)
    if int(a[0])**3 + int(a[1])**3 + int(a[2])**3 == i:
        armstrong_num.append(i)
print(armstrong_num)
#費波那係數
def fn(n):
    a=0
    b=1
    c=0
    for i in range(n):
        print(c,end=' ')
        c=a+b
        a,b=c,a

n=input()
fn(int(n))
#費波那係數 推算
def fn(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    
    return fn(n-1) +fn(n-2)
n=input()
print(fn(int(n)))

#撲克牌洗牌
color = {'桃','心','梅','磚'}
number = {'A','2','3','4','5','6','7','8','9','10','J','Q','K'}
poke = {i+j for i in color for j in number}
print(poke)
#4
a=[(i,j,k) for i in range(1, 11) for j in range(1,11) for k in range(1,11) if (i**2)+(j**2)==k**2 and (i+j+k)== 24]
print(a)

#第六章
import random

num=str(random.randint(0,9))
n=input('guess a number')
while n!=num:
  n=input('guess a number')
print('猜中了')

from functools import total_ordering

@total_ordering
class Rational:
    def __init__(self, numer:int, denom: int) -> None:
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
s1=Rational(2,5)
s2=Rational(1,5)

print(s1>s2)
print(s1>=s2)
print(s2<s1)
print(s2<=s1)
print(s1==s2)
print(s1!=s2)
