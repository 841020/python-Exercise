為了可讀性以及維護性通常不會寫巢狀判斷
## 減少條件判斷方法
- 確認範圍使用set 可以使用in 或取交集/差集/聯集等
- 需要替換值使用dict mapping

set裏面不能放set&dict&list(每一層)
dict不能用dict&list&set做key(每一層)

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
