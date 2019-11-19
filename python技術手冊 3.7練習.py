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
