- set 裏面不能放 set&dict&list(每一層)
- dict 不能用 dict&list&set 做 key(每一層)
- 需要替換值使用 dict mapping
## 減少條件判斷方法

- 確認範圍使用 set 可以使用 in 或取交集/差集/聯集等
- 為了可讀性以及維護性避免巢狀判斷
- 可以將巢狀判斷由前面的判斷給 flag 狀態把巢狀判斷攤開成平面
- 將預設值寫在判斷式前，當符合判斷式條件時才修改值

## copy

- 淺層拷貝 只有最外層(第 1 層，最上層)，不會隨之變動
- 深層拷貝每一層都不會隨之變動
- 不能更改值 tuple,set
- (tuple 是第 1 層不能更改，如果第 2 層 dict&list 就可以更改，set 是每一層都不能更改，set 不能修改項目值但是可以新增或刪除項目)
- list tuple 才能使用 slice

```python
word = 'abc'
word[1:2] = 'b'
word[slice(1, 2, None) = 'b'
```

- list tuple 能使用+直接合併項目
- liat tuple 能直接使用\*產生新的 ele
- tuple list set dict 都可用 in 因為都可迭帶
- list dict set tuple 都可以容許不同型態存在
- 在迭代物件時盡量不要對物件內容做修改
- 建議新增一個物件去做內容的刪減

```python
for x in a[:]:
    if x < 0:
        a.remove(x)
```

ex

```python
lt = list()
for item in a:
  if x < 0:
    pass
   else:
      lt.append(item)
```

## 尤其要避免使用索引迭代物件時做物件內容的刪減

```python
a = [1, 2, 3, 4, 5]
for i in range(5):
    a.remove(a[i])
```
# 可以對物件copy再迭代這樣就可以對原物件操作
```python
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
```

## finally 的優先性

- finally 的操作會在回傳前先執行
- 所以如果 finally 有 return

```python
>>> def foo():
...     try:
...         return 'try'
...     finally:
...         return 'finally'
...
>>> foo()
'finally'
```

## 避免預設值直接賦予資料結構    因為default的參考物件是固定的並不會因為重新呼叫function而重新乾淨的產生預設參考 

ex

```python
def xx(a=[]):
    pass
```

```python
def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin
```

# default value不要參考變數 因為原參考還在 是重新創造一個同樣名稱的變數 並不會被預設值參考
```python
>>> i = 5
>>> 
>>> def f(arg=i):
...     print(arg)
... 
>>> i = 6
>>> f()
5
```

## 不要用_當變數名稱

- 因為_預設為最近一次的 standard output

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

## 因為產生一個新的 a

```python
>>> a, b = 0, 1
>>> id(a)
10914464
>>> a, b = b, a+b
>>> id(a)
10914496
```

```python
x = [0, 1]
i = 0
i, x[i] = 1, 2         # i is updated, then x[i] is updated
print(x)
```
