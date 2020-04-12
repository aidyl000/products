# 先讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue # 跳到下一迴
        name, price = line.strip().split(',') 
        products.append([name, price])
print(products)
# 一個line是一行(apple, 10)，split是切割的意思，用逗點來作切割；先刪除/n，再切割
#split切割完就會變清單；每個s是一個清單
# continue 跟 break 一樣只能寫在迴圈裡
# continue通常是寫在迴圈中很高的位置

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')  
    price = int(price) # 加這個之前它是字串
    products.append([name, price]) # p = [name, price]
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: # 可寫成txt或csv檔，要有逗點才會在excel裡分成不同格
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # 加法是字串跟字串作合併，str是將之轉乘字串

# with幫你自動關閉close
# 若打開excel或將csv檔放入sublime，出現的是亂碼的話→需要編碼encoding，寫入與讀取都會牽扯到編碼
# utf-8 是最廣泛使用的編碼
# 若編碼後在sublime是正確顯示但excel仍舊亂碼的話，可於excel檔裡調整設定:
    # excel→資料→取得外部資料→從文字檔→編碼選utf-8→分隔符號選逗點

