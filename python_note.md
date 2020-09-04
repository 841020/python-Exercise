## 減少條件判斷方法
- 確認範圍使用set 可以使用in 或取交集/差集/聯集等
- 需要替換值使用dict mapping
- 為了可讀性以及維護性避免巢狀判斷
- 可以將巢狀判斷由前面的判斷給flag狀態把巢狀判斷攤開成平面

set裏面不能放set&dict&list(每一層)
dict不能用dict&list&set做key(每一層)

## coppy
淺層拷貝 只有最外層(第1層，最上層)，不會隨之變動
深層拷貝每一層都不會隨之變動

不能更改值tuple,set
(tuple是第1層不能更改，如果第2層dict&list就可以更改，set是每一層都不能更改，set不能修改項目值但是可以新增或刪除項目)

list tuple 才能使用slice
```python
word = 'abc'  
word[1:2] ='b'  
word[slice(1,2,None) = 'b'
```
list tuple能使用+直接合併項目
liat tuple 能直接使用*產生新的ele

tuple list set dict都可用in  因為都可迭帶
list dict set tuple 都可以容許不同型態存在



在迭代物件時盡量不要對物件內容做修改
建議新增一個物件去做內容的刪減
for x in a[:]:
    if x < 0: a.remove(x)
舉例
lt = list()
for item in a:
  if x<0:
    pass
   else:
      lt.append(item)

## 
尤其要避免使用索引迭代物件時做物件內容的刪減
a=[1,2,3,4,5]
for i in range(5):
    a.remove(a[i])
    
## finally的優先性
finally 的操作會在回傳前先執行
所以如果finally有return
def foo():
    try:
        return 'try'
    finally:
        return 'finally'

foo()
