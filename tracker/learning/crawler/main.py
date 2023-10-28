from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import requests
import shutil
import base64

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument('--proxy-server="direct://"')
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
#options.add_argument("--headless")

DRIVER_PATH = "chromedriver.exe" #chromedriverの場所
driver = webdriver.Chrome()

query = input('Search word? :')
url = ("https://www.google.com/search?hl=jp&q=" + "+".join(query.split()) + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
driver.get(url)

#適当に下までスクロールしてる--
for t in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1.5)
try:
    driver.find_element_by_class_name("mye4qd").click() #「検索結果をもっと表示」ってボタンを押してる
except:
    pass

for t in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1.5)

srcs = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
try:os.mkdir(query) #検索語と同じ名前のフォルダを作る、保存先
except:pass
#--

i = 0 #ファイル名に通し番号をつける用カウンタ

print("Downloading...")
for j, src in enumerate(srcs):
    if j % 50 == 0 or j == len(srcs)-1:
        print("|"+ ("■" * (20 * j // (len(srcs)-1)))+ (" -" * (20 - 20 * j // (len(srcs)-1)))+ "|",f"{100*j//(len(srcs)-1)}%") #ダウンロードの進捗示すやつ
    file_name = f"{query}/{'_'.join(query.split())}_{str(i).zfill(3)}.jpg" #ファイル名とか場所とか
    src = src.get_attribute("src")
    if src != None:
#画像に変換--
        if "base64," in src:
            with open(file_name, "wb") as f:
                f.write(base64.b64decode(src.split(",")[1]))
        else:
            res = requests.get(src, stream=True)
            with open(file_name, "wb") as f:
                shutil.copyfileobj(res.raw, f)
#--
        i += 1

driver.quit() #ウィンドウを閉じる
print(f"Download is complete. {i} images are downloaded.")
