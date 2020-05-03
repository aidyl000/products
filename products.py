import os # operating system(作業系統模組)
# 讀取檔案
def read_file(filename):
    products = [] # 不管有沒有找到檔案，都要產生這個清單，所以放在if的上面
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 跳到下一迴
            name, price = line.strip().split(',') 
            products.append([name, price])
    return products # 回傳存成清單

# os中有一個叫path的模組，模組中有一個叫isfile的功能
# 一個line是一行(apple, 10)，split是切割的意思，用逗點來作切割；先刪除/n，再切割
# split切割完就會變清單；每個s是一個清單
# continue 跟 break 一樣只能寫在迴圈裡
# continue通常是寫在迴圈中很高的位置

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入商品價格:')  
        price = int(price) # 加這個之前它是字串
        products.append([name, price]) # p = [name, price]
    print(products)
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f: # 可寫成txt或csv檔，要有逗點才會在excel裡分成不同格
        f.write('商品,價格\n') # title
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') # 加法是字串跟字串作合併，str是將之轉乘字串
# with幫你自動關閉close
# 若打開excel或將csv檔放入sublime，出現的是亂碼的話→需要編碼encoding，寫入與讀取都會牽扯到編碼
# utf-8 是最廣泛使用的編碼
# 若編碼後在sublime是正確顯示但excel仍舊亂碼的話，可於excel檔裡調整設定:
    # excel→資料→取得外部資料→從文字檔→編碼選utf-8→分隔符號選逗點

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 只給檔名是相對路徑(比如在與程式檔相同的資料夾)，給地址是絕對路徑
        print('yeah! the file is found!')
        products = read_file(filename)
    else:
        print('the file cannot be found')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main() # 程式最好有main() function作為程式進入點