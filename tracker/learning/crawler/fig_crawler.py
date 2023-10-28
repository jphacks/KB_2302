from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import requests
import shutil
import base64


targets = [
    "key",
    "smartphone",
    "pencil case",
    "earphone",
    "mouse",
    "remote controller",
    "wristwatch",
    "tobacco",
]

# このファイルのディレクト理を入手
BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

# 画像を保存するディレクトリがなければ作る
FIGURRES_DIR = os.path.join(BASE_DIR, 'figures')
if not os.path.exists(FIGURRES_DIR):
    os.mkdir(FIGURRES_DIR)


def main(target :str):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument('--proxy-server="direct://"')
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")

    DRIVER_PATH = "chromedriver.exe" #chromedriverの場所
    driver = webdriver.Chrome()

    query = target
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
    try:
        os.mkdir(
            os.path.join(FIGURRES_DIR, query)
            ) #検索語と同じ名前のフォルダを作る、保存先
    except:pass
    #--

    i = 0 #ファイル名に通し番号をつける用カウンタ

    print("Downloading...")
    for j, src in enumerate(srcs):
        if j % 50 == 0 or j == len(srcs)-1:
            print("|"+ ("■" * (20 * j // (len(srcs)-1)))+ (" -" * (20 - 20 * j // (len(srcs)-1)))+ "|",f"{100*j//(len(srcs)-1)}%") #ダウンロードの進捗示すやつ
        file_name = f"{'_'.join(query.split())}_{str(i).zfill(3)}.jpg" #ファイル名とか場所とか
        file_name = os.path.join(os.path.join(FIGURRES_DIR, query), file_name)
        
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

if __name__ == '__main__':
    
    for target in targets:
        main(target)
