# 如果要自訂字串格式化寬度可以使用打藥設定的寬度放在format裡面{:{}d}這樣調用 就可以擺脫數字限制
n=len('{:b}'.format(number))
    for i in range(1,number+1):
        print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(i, width=n))
 for i in range(20):
 #這兩個16進為差別在於英文大小寫
  print('{:x} {:X}'.format(i)

#input 輸入 克隔壁免背重組
a=input() #123  456
# '123 456'
set(a)
#{'1', '2', '3', '4', '5', '6', ' '}
set(a.split())
#{'123', '456'}
        
a = input().split()
b=[i+j for i in a[0] for j in a[0] ]
b.sort()

for i in b:
    if i == i[::-1]:
        del i
        continue
    print(i)
