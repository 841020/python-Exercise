#當你的模組以字串的方式傳入方法或函數
#這時候會需要使用動態導入 導入模組

#在此提供一個個人在工作上的實踐

import os
import sys

def foo(module):
  module_path = '{}/{}'.format(os.getcwd(), module_directory)
  
  sys.path.append(module_path)
  
  module = __import__(module)
  
  module.action()
  
  
# 如果模組路徑跟當前程式碼執行目錄不同，就會需要將模組目錄加入sys.path，因為 __import__只會抓取sys.path裡面的路徑
# 需要特別注意模組檔名是否與原先添加在sys.path路徑裡面的檔名重複，因為__import__似乎是依照sys.path的index順序的目錄去尋找模組，
# 若重複可能導致import的模組錯誤，而無法使用鴨子定型
# 這種提供一個情境 例如你有一整個目錄的模組樣板(例如產生pdf/excel的程式碼)
# 只要前端告訴後端現在要套哪個要樣板，後端就會將模組目錄加入sys.path，然後就能夠使用鴨定型執行套入樣板的動作
